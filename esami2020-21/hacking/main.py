#Apro il file prodotti.txt
infile_prodotti = "prodotti.txt"
file_prodotti = open(infile_prodotti, "r", encoding="UTF-8")

#Creo e riempo il dizionario dei prodotti
dict_prodotti = {}
for riga_prodottti in file_prodotti:
    temp_list_prodotti = riga_prodottti.rstrip().split(" ")
    dict_prodotti[temp_list_prodotti[0]] = temp_list_prodotti[1]

#Chiudo il file prodotti.txt
file_prodotti.close()

#Apro il file acquisti.txt
infile_acquisti = "acquisti.txt"
file_acquisti = open(infile_acquisti, "r", encoding="UTF-8")

#Creo e riempo il dizionario degli acquisti
dict_acquisti = {}
for riga_acquisti in file_acquisti:
    temp_list_acquisti = riga_acquisti.rstrip().split(" ")
    dict_acquisti[temp_list_acquisti[0]] = temp_list_acquisti[1]

#Chiudo il file acquisti.txt
file_acquisti.close()

#Gestisco le vendite fraudolente
print(f"Elenco transizioni sospette: ")
for key, val in dict_prodotti.items():
    if key in dict_acquisti:
        if dict_acquisti[key] != val:
            print(f"Codice prdotto: {key}")
            print(f"Rivenditore ufficiale: {val}")
            print(f"lista rivenditori: {val} {dict_acquisti[key]}\n")

