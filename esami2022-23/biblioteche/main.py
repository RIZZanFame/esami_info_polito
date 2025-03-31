infile = "inventarioOld.csv"
file = open(infile, "r", encoding="UTF-8")

dizionario_inventario = {}
for riga in file:
    riga = riga.rstrip().split(";")
    tripla = (riga[0], riga[2], riga[3])
    ISBN = riga[1]

    if ISBN not in dizionario_inventario:
        dizionario_inventario[ISBN] = []
    
    dizionario_inventario[ISBN].append(tripla)

file.close()

file = open("inventarioScuola.csv", "w", encoding="UTF-8")

libri_regalati = 0
tot_copie_regalate = 0

inventario_new = {}

for codice, libri in dizionario_inventario.items():
    if len(libri) >= 3:
        libri_regalati += 1
        copie_regalate = (len(libri) - 3)
        tot_copie_regalate += copie_regalate
        file.write(f"{codice};{libri[0][1]};{libri[0][2]}")
        for i in range(0, (len(libri) - 3)):
            file.write(f";{libri[i][0]}")
        file.write("\n")

        inventario_new[(codice, libri[0][1], libri[0][2])] = []
        for i in range((len(libri) - 3), len(libri)):
            inventario_new[(codice, libri[0][1], libri[0][2])].append(libri[i][0])
    elif len(libri) < 3:
        inventario_new[(codice, libri[0][1], libri[0][2])] = libri[0][0]

file.close()
print(f"Numero libri da regalare: {libri_regalati}, copie totali: {tot_copie_regalate}")
print()