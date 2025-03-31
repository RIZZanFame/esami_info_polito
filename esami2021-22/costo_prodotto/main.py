infile = input("Inserisci il nome del file: ")
preziario = open(infile, "r", encoding="UTF-8")

dizionario_preziario = {}
for riga in preziario:
    riga = riga.rstrip()
    stato, valuta, prezzo = riga.split(";")
    lista_prezzo_stato = [int(prezzo), stato]
    dizionario_preziario[valuta] = lista_prezzo_stato

preziario.close()

infile = "exchange.txt"
forex = open(infile, "r", encoding="UTF-8")

diz_lista = {}
for riga in forex:
    riga = riga.rstrip()
    moneta, tasso = riga.split("\t")
    for valuta, info in dizionario_preziario.items():
        if valuta == moneta:
            diz_lista[info[1]] = float(tasso) * info[0]

forex.close()

lista_ordinata = sorted(diz_lista.items(), key=lambda x: x[1])
print(f"\nIl paese dove il prodotto costa meno è: {lista_ordinata[0][0]}")
print(f"Prezzo in Euro: {lista_ordinata[0][1]:.2f}\n")
print(f"Il paese dove il prodotto costa di più è: {lista_ordinata[-1][0]}")
print(f"Prezzo in Euro: {lista_ordinata[-1][1]:.2f}\n")
