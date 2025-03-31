infile = "lista.csv"
lista = open(infile, "r")

#Creo una lista di quello che, chi non è andato a fare la spesa desidera sotto forma di dizionario
dizionario_lista = {}
for riga in lista:
    prodotto, quantità = riga.rstrip().split(",")
    dizionario_lista[prodotto] = int(quantità)

lista.close()

infile = "scontrino.csv"
scontrino = open(infile, "r")

#Creo un dizionario dello scontrino
dizionario_scontrino = {}
for riga in scontrino:
    prodotto, prezzo = riga.rstrip().split(",")
    #Se il prodotto è già nel dizionario aumento la quantità
    if prodotto in dizionario_scontrino:
        quantità = dizionario_scontrino[prodotto][1]
        dizionario_scontrino[prodotto] = (float(prezzo), quantità + 1)
    else:
        dizionario_scontrino[prodotto] = (float(prezzo), 1)

scontrino.close()

#Calcolo quanto deve chi non ha fatto la spessa al coinquilino
totale_dovuto = 0
for prodotto, quantità in list(dizionario_lista.items()):
    if prodotto in dizionario_scontrino:
        if quantità <= dizionario_scontrino[prodotto][1]:
            totale_dovuto += (quantità * dizionario_scontrino[prodotto][0])
            dizionario_lista.pop(prodotto)
        else:
            totale_dovuto += (dizionario_scontrino[prodotto][0] * dizionario_scontrino[prodotto][1])
            dizionario_lista[prodotto] -= dizionario_scontrino[prodotto][1]

#Calcolo il totale dell spesa
totale_spesa = 0
for riga in dizionario_scontrino:
    prezzo_quantità = dizionario_scontrino[riga]
    totale_spesa += (prezzo_quantità[0] * prezzo_quantità[1])

#Stampo a video quanto richiesto
print(f"Totale spesa: {totale_spesa:.2f} euro")
print(f"Totale dovuto: {totale_dovuto:.2f} euro")
print("\nProdotti mancanti:")
for prodotto, quantità in dizionario_lista.items():
    print(f"{prodotto}, {quantità}")