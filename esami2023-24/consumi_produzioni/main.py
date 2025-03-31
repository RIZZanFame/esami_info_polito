infile = "consumi.txt"
file = open(infile, "r", encoding="UTF-8")

dizionario_consumi_giornata = {}
file.readline()
for riga in file:
    riga = riga.rstrip().split(";")
    consumo = float(riga[3])
    if riga[0] not in dizionario_consumi_giornata:
        dizionario_consumi_giornata[riga[0]] = []
    
    dizionario_consumi_giornata[riga[0]].append(consumo)


consumo_tot = 0
for i, consumi in dizionario_consumi_giornata.items():
    consumo_giorno = sum(consumi)
    consumo_tot += consumo_giorno
    dizionario_consumi_giornata[i] = consumo_giorno

file.close()
#--------------------------------------------------------
infile = "impianti.txt"
file = open(infile, "r", encoding="UTF-8")

file.readline()
dizionario_potenze_case = {}
for riga in file:
    riga = riga.rstrip().split(";")
    dimensione_imp = float(riga[1])
    effic = float(riga[2])
    potenziale = dimensione_imp * effic
    dizionario_potenze_case[riga[0]] = (potenziale)

file.close()
#-------------------------------------------------------
infile = "meteo.txt"
file = open(infile, "r", encoding="UTF-8")

file.readline()
dict_produzione = {}
for riga in file:
    riga = riga.rstrip().split(";")
    for ID, power in dizionario_potenze_case.items():
        prod_istantanea = power * float(riga[2])
        if ID not in dict_produzione:
            dict_produzione[ID] = []
        dict_produzione[ID].append(prod_istantanea)

produzione_tot = 0
for ID, prod_nel_giorno in dict_produzione.items():
    prod_giornaliera = sum(prod_nel_giorno)
    produzione_tot += prod_giornaliera
    dict_produzione[ID] = prod_giornaliera

file.close()
#-----------------------------------------------------------


