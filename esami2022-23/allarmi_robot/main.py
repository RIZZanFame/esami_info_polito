infile = "allarmi.csv"
file = open(infile, "r", encoding="UTF-8")

file.readline()
dizionario_allarmi = {}
for riga in file:
    riga = riga.rstrip().split(";")
    chiave = riga[0]
    valore = int(riga[1])
    if chiave not in dizionario_allarmi:
        dizionario_allarmi[chiave] = []

    dizionario_allarmi[chiave].append(valore)

file.close()

lista_allarmi = []
for chiave, valore in dizionario_allarmi.items():
    specifiche = (chiave, len(valore))
    lista_allarmi.append(specifiche)

lista_allarmi = sorted(lista_allarmi, key=lambda x: x[1], reverse=True)
for i in lista_allarmi:
    print(f"Per il robot {i[0]}, si sono verificate {i[1]} anomalie")

lista_allarmi = []
for chiave, valore in dizionario_allarmi.items():
    valore_massimo_robot = max(valore)
    specifiche = (chiave, valore_massimo_robot)
    lista_allarmi.append(specifiche)

massimo = max(lista_allarmi, key=lambda x: x[1])

print()
print(f"Il valore massimo di criticità {massimo[1]} è stato raggiunto dai robot:")
for i in lista_allarmi:
    if i[1] == massimo[1]:
        print(i[0])    