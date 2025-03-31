from csv import reader

infile = "sportivi.csv"
sportiti = open(infile, "r")
csvReader = reader(sportiti)

dizionario_calciatori = {}
for riga in csvReader:
    data = riga[3].split("/")
    dizionario_calciatori[riga[0]] = (int(riga[1]), (data[1]+data[0]))

sportiti.close()

infile = "zodiaco.csv"
zodaico = open(infile, "r")
csvReader = reader(zodaico)

dizionario_zodiaco = {}
for riga in csvReader:
    data_inizio = riga[1].split("/")
    data_inizio = data_inizio[1] + data_inizio[0]
    data_fine = riga[2].split("/")
    data_fine = data_fine[1] + data_fine[0]
    dizionario_zodiaco[riga[0]] = (data_inizio, data_fine)

zodaico.close()

dizionario_classifica = {}
for segno, date in dizionario_zodiaco.items():
    goal_segno_zodiaco = 0
    data_inizio = date[0]
    data_fine = date[1]
    for calciatore, goal_segno in dizionario_calciatori.items():
        nascita = goal_segno[1]
        goal_calciatore = goal_segno[0]
        if nascita <= data_fine and nascita >= data_inizio:
            goal_segno_zodiaco += goal_calciatore
            dizionario_classifica[segno] = goal_segno_zodiaco

lista_classifica = sorted(dizionario_classifica.items(), key=lambda x: x[1], reverse=True)
for i in lista_classifica:
    print(f"{i[0]}, {str(i[1])} {'*' * (int(i[1]/116))}")