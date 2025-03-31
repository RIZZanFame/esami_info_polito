infile = "ordine.txt"
file = open(infile, "r", encoding="UTF-8")

dizionario_ordine = {}
for riga in file:
    ID, quantità = riga.rstrip().split(",")
    dizionario_ordine[ID] = int(quantità)

file.close()

infile = "menu.txt"
file = open(infile, "r", encoding="UTF-8")

dizionario_scontrino = {}
for riga in file:
    temp_list = riga.rstrip().split(",")
    if temp_list[0] in dizionario_ordine:
        quantità = dizionario_ordine[temp_list[0]]
        prezzo_in_scontrino_ivato = quantità * float(temp_list[2])
        IVA = int(temp_list[3])
        tasse = ((prezzo_in_scontrino_ivato/100) * int(temp_list[3]))
        quadrupla = (prezzo_in_scontrino_ivato, tasse, IVA, quantità)
        dizionario_scontrino[temp_list[1].lstrip()] = quadrupla

file.close()

totale_pagato = 0
totale_tasse = 0
for piatto, prezzi in dizionario_scontrino.items():
    totale_pagato += prezzi[0]
    totale_tasse += prezzi[1]

dizionario_ordinato = dict(sorted(dizionario_scontrino.items(), key=lambda item: item[1][2]))

print(f"\nTotale: € {totale_pagato:.2f} ")
print(f"Di cui IVA € {totale_tasse:.2f}")



