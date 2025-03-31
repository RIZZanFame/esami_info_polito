#Apro i file in lettura 
infile = "dogs.csv"
file = open(infile, "r", encoding="UTF-8")

#Scarto la prma riga d'intestazione
file.readline()

#Creo un dizionario generale che ha come valore il nome della razza
dizionario_canile = {}
for riga in file:

    #Elaboro la riga in esame
    riga = riga.rstrip().split(",")

    #Creo variabili parlanti
    razza = riga[2]
    livello = riga[3]
    score = float(riga[4])

    #Controllo che la razza non sia già nel dizionario
    if razza not in dizionario_canile:
        #Se la razza è nel dict, creo un dict intermedio che storerà i dati
        dizionario_intermedio = {}
        dizionario_canile[razza] = dizionario_intermedio

    dizionario_intermedio = dizionario_canile[razza]
    
    #Controllo che il livello non sia già nel dizionario intermedio
    if livello not in dizionario_intermedio:
        dizionario_intermedio[livello] = []
        
    #Appendo i dati
    dizionario_intermedio[livello].append(score)

#Chiudo il file
file.close()

#Stampo a video le medie dei vari livelli delle varie razze
punteggio_max = 0
for razza, livelli in dizionario_canile.items():
    print(f"\nRazza: {razza}")
    for livello, punteggi in livelli.items():
        media_punteggio = sum(punteggi) / len(punteggi)
        print(f"    {livello}: media {media_punteggio:.2f}")
        if livello == "Expert":
            if media_punteggio > punteggio_max:
                punteggio_max = media_punteggio
                razza_beast = razza

print(f"\nLa razza con il punteggio medio più alto per il livello Expert è {razza_beast}")