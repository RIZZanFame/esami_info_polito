infile = "shops.txt"
file = open(infile, "r", encoding="UTF-8")

mercati = []
for riga in file:
    mercato = riga.rstrip()
    mercati.append(mercato)

file.close()

infile = "NLFoodPricing.csv"
file = open(infile, "r", encoding="UTF-8")

file.readline()

dizionario_supermercati = {}
prodotti_essenziali = set()

for riga in file:
    riga = riga.rstrip().split(",")
    luogo = riga[2]
    prodotto = riga[3]
    essenziale = riga[4]
    prezzo = float(riga[5])

    if essenziale == "E":
        if luogo in mercati:
            prodotti_essenziali.add(prodotto)
            if luogo not in dizionario_supermercati:
                dizionario_supermercati[luogo] = {}
            if prodotto not in dizionario_supermercati[luogo]:
                dizionario_supermercati[luogo][prodotto] = prezzo
            else:
                dizionario_supermercati[luogo][prodotto] = min(dizionario_supermercati[luogo][prodotto], prezzo)

file.close()

prodotti_essenziali = sorted(prodotti_essenziali)

# Stampa prodotti essenziali
print("Prodotti:")
for prodotto in prodotti_essenziali:
    print(f"- {prodotto}")
print()

# Stampa prezzi per supermercato
for mercato in sorted(mercati):
    print(f"{mercato}:")
    if mercato in dizionario_supermercati:
        for prodotto in prodotti_essenziali:
            if prodotto in dizionario_supermercati[mercato]:
                prezzo = dizionario_supermercati[mercato][prodotto]
                print(f"- {prodotto}: {prezzo:.2f} $/kg")
            else:
                print(f"- {prodotto}: Non disponibile")
    else:
        print("- Nessun dato disponibile")
    print()

# Ricerca del prezzo minimo per prodotto
uscita = False
while not uscita:
    ricerca = input("Che cibo vuoi cercare? (q per smettere) ")
    if ricerca == "q":
        print("Arrivederci")
        uscita = True
    elif ricerca in prodotti_essenziali:
        prezzo_minimo = None
        mercato_minimo = None
        for mercato, prodotti in dizionario_supermercati.items():
            if ricerca in prodotti:
                if prezzo_minimo is None or prodotti[ricerca] < prezzo_minimo:
                    prezzo_minimo = prodotti[ricerca]
                    mercato_minimo = mercato
        if prezzo_minimo is not None:
            print(f"Prezzo minimo: {prezzo_minimo:.2f} $/kg da {mercato_minimo}")
        else:
            print(f"{ricerca} non disponibile in alcun mercato")
    else:
        print(f"Cibo {ricerca} non trovato")

