infile = "storicoShort.txt"
file = open(infile, "r", encoding="UTF-8")

dizionario_estrazione = {}
for riga in file:
    riga = riga.rstrip().split("\t")
    città = riga[1]
    data = riga[0]
    estrazioni = riga[2:]

    if città not in dizionario_estrazione:
        dizionario_estrazione[città] = {}
    
    dizionario_estrazione[città][data] = estrazioni

file.close()

#Printo a video tutte le ruote disponibili
print("Ruote disponibile: ", end="")
for città in dizionario_estrazione:
    print(f"{città}, ", end="")
#Annullo il ciclo della end=""
print()

#Chiedo all'utente di inserire la citta (potrà anche inserirle minuscole)
prima_ruota = input("Inserisci la prima ruota: ").upper()
seconda_ruota = input("Inserisci la seconda ruota: ").upper()

if prima_ruota and seconda_ruota not in dizionario_estrazione:
    print("\nLe città da te inserite non sono luoghi di estrazione, ritenta: \n")
    prima_ruota = input("Inserisci la prima ruota: ")
    seconda_ruota = input("Inserisci la seconda ruota: ")

dizionario_frequenza = {}


if prima_ruota and seconda_ruota in dizionario_estrazione:
    for data_1, estrazioni_1 in dizionario_estrazione[prima_ruota].items():
        for data_2, estrazioni_2 in dizionario_estrazione[seconda_ruota].items():
            for estrazione_1 in estrazioni_1:
                for estrazione_2 in estrazioni_2:
                    if estrazione_1 == estrazione_2:
                        print(f"Numero comune {estrazione_1} in data {data_1}")
                        numero = estrazione_1
                        if numero not in dizionario_frequenza:
                            dizionario_frequenza[numero] = 1
                        else:
                            dizionario_frequenza[numero] += 1

#Sorto un nuovo dizionario per stampare a video i numeri "magici"
frequenza_sortato = dict(sorted(dizionario_frequenza.items(), key=lambda x: x[1], reverse=True))

print("\nNumero    Frequenza")
print("-" * 20)
#Intendo la stampa in modo tale che ogni numero occupi 10 spazi
for numero, frequenza in frequenza_sortato.items():
    print(f"{numero:<10}        {frequenza:<10}")
                        
    
