from operator import itemgetter

costiFile = open("costipagine.txt", "r")
costi = []

for line in costiFile:
    data = line.strip(" €\n").split(";")
    costi.append([int(data[1]),float(data[2])])

costi.sort(key=itemgetter(0))

for (limite,costo) in costi:
    print(f"Fino a {limite:5} pagine: {costo:3.1f}€/pagina")

nomeIn = input("Nome file: ")
libriFile = open(nomeIn, "r")
print()
#libriFile = open("libri.txt", "r")

tabellaFinale = {}
for riga in libriFile:
    (titolo, pagine) = riga.strip().split(";")
    pagine = int(pagine)
    #devo trovare la chiave più piccola con n pagine > pagine del libro
    nPagine = -1
    nCosto = 0
    for limPag,limCosto in costi:
        if pagine < limPag:
            if nPagine == -1 or limPag < nPagine:
                nPagine = limPag
                nCosto = limCosto
    tabellaFinale[titolo] = [pagine,nCosto*pagine]

totale = 0
#print (tabellaFinale)
for (titolo) in sorted(tabellaFinale):
    print(f"{titolo:25}- Pagine: {tabellaFinale[titolo][0]:8} - Costo: {tabellaFinale[titolo][1]:8.2f}€")
    totale += tabellaFinale[titolo][1]

print(f"Total: {totale:10.2f}€")
