from csv import reader

infile = "elenco-comuni-italiani.csv"
file = open(infile, "r", encoding="UTF-8")
csvReader = reader(file)

#Creo un dizionario che ha come chiave il nome della regione e valore la lista dei suoi comuni
next(csvReader)
dizionario_comuni = {}
for riga in csvReader:
    temp_list = riga[0].split(";")
    if temp_list[10] in dizionario_comuni:
        lista_regione = dizionario_comuni[temp_list[10]]
        lista_regione.append(temp_list[6])
        dizionario_comuni[temp_list[10]] = lista_regione
    else:
        dizionario_comuni[temp_list[10]] = [temp_list[6]]

file.close()

infile = "regioni.txt"
regioni = open(infile, "r", encoding="UTF-8")

#Stampo a video le specifiche richieste della regione contenuta nel file regioni.txt
for regione in regioni:
    regione = regione.rstrip()
    if regione in dizionario_comuni:
        numero_comuni_regione = len(dizionario_comuni[regione])
        comune_piu_lungo = max(dizionario_comuni[regione], key=lambda comune: (len(comune), comune))
        comune_piu_corto = min(dizionario_comuni[regione], key=lambda comune: (len(comune), comune))
        print(f"\n*** REGIONE {regione} ***")
        print(f"La regione {regione} ha {numero_comuni_regione} Comuni")
        print(f"Il nome più breve è {comune_piu_corto} e quello più lungo è {comune_piu_lungo}")
    else:
        print(f"Hai scritto *{regione}* è sbagliato")
    
regioni.close(  )