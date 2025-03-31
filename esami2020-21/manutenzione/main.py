#Apro il file manutenzione.txt in lettura
infile_manutenzione = "manutenzione.txt"
file_manutenzione = open(infile_manutenzione, "r", encoding="UTF-8")

#Creo un dizionario dove salvare i dati in manutenzione.txt
dict_manutenzione = {}
for riga_manut in file_manutenzione:
    riga_temp_manut = riga_manut.rstrip().split(",")
    data_str = riga_temp_manut[1]
    data_dict = data_str.split("/")
    i = 0
    for element in data_dict:
        element = int(element)
        data_dict[i] = element
        i += 1
    data_dict.append(int(riga_temp_manut[2]))
    dict_manutenzione[riga_temp_manut[0]] = data_dict

#Apro il file parametri.txt in lettura
infile_parametri = "parametri.txt"
file_parametri = open(infile_parametri, "r", encoding="UTF-8")

#Per ogni riga del file splitto la data e il parametro
for riga_par in file_parametri:
    riga_temp_par = riga_par.rstrip().split(",")
    parametro = riga_temp_par[1]
    data_str = riga_temp_par[0]
    data_list = data_str.split("/")

#Se parametro == a, stampo a video le operazioni prima della data
if parametro == "a":
    print(f"Le operazione effettuate prima del {data_str} sono:\n")
    for (key,elemento) in dict_manutenzione.items():
        if int(data_list[2]) > elemento[2]:
            print(f"{key}, in data {elemento[0]}/{elemento[1]}/{elemento[2]} costo {elemento[3]}€")
        elif int(data_list[2]) == elemento[2]:
            if int(data_list[1]) > elemento[1]:
                print(f"{key}, in data {elemento[0]}/{elemento[1]}/{elemento[2]} costo {elemento[3]}€")
            elif int(data_list[1]) == elemento[1]:
                if int(data_list[0]) >= elemento[0]:
                    print(f"{key}, in data {elemento[0]}/{elemento[1]}/{elemento[2]} costo {elemento[3]}€")

#Se parametro == p, stampo a video le operazioni dopo la data
elif parametro == "p":
    print(f"Le operazione effettuate dopo il {data_str} sono:\n")
    for (key,elemento) in dict_manutenzione.items():
        if int(data_list[2]) < elemento[2]:
            print(f"{key}, in data {elemento[0]}/{elemento[1]}/{elemento[2]} costo {elemento[3]}€")
        elif int(data_list[2]) == elemento[2]:
            if int(data_list[1]) < elemento[1]:
                print(f"{key}, in data {elemento[0]}/{elemento[1]}/{elemento[2]} costo {elemento[3]}€")
            elif int(data_list[1]) == elemento[1]:
                if int(data_list[0]) <= elemento[0]:
                    print(f"{key}, in data {elemento[0]}/{elemento[1]}/{elemento[2]} costo {elemento[3]}€")

#Chiudo i file
file_manutenzione.close()
file_parametri.close()

    