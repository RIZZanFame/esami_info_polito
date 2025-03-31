infile = "glucometers.txt"
file = open(infile, "r", encoding="UTF-8")

dizionario_pazienti = {}
for riga in file:
    lista_paziente = []
    temp_list = riga.rstrip().split(" ")
    codice_paziente = temp_list[0]
    tupla_info_paziente = (temp_list[1], int(temp_list[2]))
    if codice_paziente in dizionario_pazienti:
        dizionario_pazienti[codice_paziente].append(tupla_info_paziente)
    else:
        dizionario_pazienti[codice_paziente] =[tupla_info_paziente]

file.close()

for chiave, valore in dizionario_pazienti.items():
    for ore, esito in valore:
        if esito >= 200:
            print(f"{chiave} {ore} {esito}")
    print("")
    
    