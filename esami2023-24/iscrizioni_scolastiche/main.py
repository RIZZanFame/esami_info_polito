infile = "regpie-studenti.csv"
file = open(infile, "r", encoding="UTF-8")

file.readline()
dizionario_scuole = {}
for riga in file:
    temp_list = riga.rstrip().strip('""').split('","')
    code_tipo_scuola = temp_list[3][0]
    info_scuola = (code_tipo_scuola, int(temp_list[8]))
    if temp_list[1] not in dizionario_scuole:
        dizionario_scuole[temp_list[1]] = []
    
    dizionario_scuole[temp_list[1]].append(info_scuola)
    
lista_ordinata = sorted(dizionario_scuole)

print("Le province per le quali vengono fornite le statistiche sono:")
for provincia in lista_ordinata:
    print(provincia)

print()
studenti_infanzia = 0
for provincia in lista_ordinata:
    if provincia in dizionario_scuole:
        scuole = dizionario_scuole[provincia]
        totale_studenti = 0
        for num in scuole:
            totale_studenti += num[1]
            if num[0] == "1":
                studenti_infanzia += num[1]
        print(f"Totale studenti iscritti {provincia}: {totale_studenti}")

print()
print(f"Gli studenti iscritti alla scuola dell'infanzia in Piemonte sono: {studenti_infanzia}")