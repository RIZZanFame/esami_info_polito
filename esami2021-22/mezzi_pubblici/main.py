infile = "dati_aeroporto_torino.csv"
file = open(infile, "r", encoding="UTF-8")

#Uso la prima riga del file "intestazione" per estrapolare il codice delle fermate
intestazione = file.readline().strip().split(",")
lista_fermate = intestazione[2:]

#Creo i dizionari che mi serviranno
dizionario_fermate = {}
dizionario_autisa = {}
for fermata in lista_fermate:
    dizionario_fermate[fermata] = []

for riga in file:
    riga = riga.rstrip().split(",")
    passseggeri = riga[2:]
    autista = riga[0]
    
    #Itero 
    for passeggero, fermata in zip(passseggeri, dizionario_fermate):
        passeggero = passeggero.split("/")
        if len(passeggero) <= 1:
            passeggero = passeggero[0]
            if passeggero.isdigit():
                passeggero = int(passeggero)
            else:
                if passeggero == "--":
                    passeggero = 0
                elif passeggero[0] == "-":
                    passeggero = 0 - int(passeggero[1:])
        else:
            positivo = int(passeggero[0])
            neg = passeggero[1]
            negativo = 0 - int(neg)
            passeggero = positivo - negativo
        if autista not in dizionario_autisa:
            dizionario_autisa[autista] = []

        dizionario_fermate[fermata].append(passeggero)
        dizionario_autisa[autista].append(passeggero)

file.close()

for fermata, passeggeri in dizionario_fermate.items():
    dizionario_fermate[fermata] = sum(passeggeri)

dizionario_autista_positivo = {}
for autista, passeggeri in dizionario_autisa.items():
    for passeggero in passeggeri:
        if passeggero >= 0:
            if autista not in dizionario_autista_positivo:
                dizionario_autista_positivo[autista] = []
            dizionario_autista_positivo[autista].append(passeggero)

for autista, passeggeri in dizionario_autista_positivo.items():
    dizionario_autista_positivo[autista] = sum(passeggeri)

#Sorto i dizionari creando una "classifica" per ogni item
dizionario_autista_positivo = dict(sorted(dizionario_autista_positivo.items(), key=lambda x: x[1], reverse=True))
dizionario_fermate = dict(sorted(dizionario_fermate.items(), key=lambda x: x[1], reverse=True))
maggiore_fermata = max(dizionario_fermate, key=lambda x: x[1])

num_passeggeri_maggiore_fermata = dizionario_fermate[maggiore_fermata]

infile = "database.txt"
file = open(infile, "r", encoding="UTF-8")

dizionario_nomi_autisti = {}
dizionario_nomi_fermate = {}
for riga in file:
    riga = riga.rstrip().split(":")
    
    if riga[0][0] == "A":
        dizionario_nomi_autisti[riga[0]] = riga[1].lstrip()
    elif riga[0][0] == "F":
        dizionario_nomi_fermate[riga[0]] = riga[1].lstrip()

file.close()

print(f"\nLa fermata in cui salgono più passeggeri ({num_passeggeri_maggiore_fermata}) è {dizionario_nomi_fermate[maggiore_fermata]}")

print("\nLista di autisti ordinata in base al numero di passeggeri:")
for autista, passeggeri in dizionario_autista_positivo.items():
    for codice, nome_autista in dizionario_nomi_autisti.items():
        if codice == autista:
            print(f"{nome_autista}  con {passeggeri}")

print()