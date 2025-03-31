#Apro il file costipagine.txt
infile = "costipagine.txt"
file = open(infile, "r", encoding="UTF-8")

#Gestisco la creazione del dizionario di costipagine.txt
dict_costipagine = {}
for riga in file:
    temp_list = riga.strip(" \n€").split(";")
    dict_costipagine[(int(temp_list[0]),int(temp_list[1]))] = temp_list[2]

#Stampo a video in ordine i listini prezzi
list_costipagine = sorted(dict_costipagine)
print("listino prezzi:\n")
for i in list_costipagine:
    if i in dict_costipagine:
        prezzo = dict_costipagine[i]
    print(f"fino a {str(i[1])}: {prezzo}€ per pagine ")

file.close()

#Apro il file richiesto dall'utente
outfile = input(f"\nNome del file: ")
file_out = open(outfile, "r", encoding="UTF-8")

#Gestisco la creazione del dizionario di libri.txt
dict_libri = {}
for rigo in file_out:
    temp_lista = rigo.rstrip().split(";")
    dict_libri[temp_lista[0]] = temp_lista[1]

file_out.close()

#Stampo a video i prezzi dei vari libri
list_libri = sorted(dict_libri)
print(f"\nCOSTI DI STAMPA\n")
for libri in list_libri:
    pagine_libro = int(dict_libri[libri])
    for Range in list_costipagine:
        if pagine_libro > Range[0] and pagine_libro < Range[1]:
            costo_libro = pagine_libro * float(dict_costipagine[Range])
            print(f"{libri} -pagine {str(pagine_libro)} -costo: {costo_libro:.2f}€")