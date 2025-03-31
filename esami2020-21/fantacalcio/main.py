infile = "fantacalcio.txt"
file = open(infile, "r", encoding="UTF-8")

lista_portieri = []
lista_difensori = []
lista_centrocampisti = []
lista_attacanti = []

for riga in file:
    temp_list = riga.rstrip().split(", ")
    if temp_list[2] == "portiere":
        tupla = (int(temp_list[3]), temp_list[0])
        lista_portieri.append(tupla)
    elif temp_list[2] == "difensore":
        tupla = (int(temp_list[3]), temp_list[0])
        lista_difensori.append(tupla)
    elif temp_list[2] == "centrocampista":
        tupla = (int(temp_list[3]), temp_list[0])
        lista_centrocampisti.append(tupla)
    elif temp_list[2] == "attaccante":
        tupla = (int(temp_list[3]), temp_list[0])
        lista_attacanti.append(tupla)

file.close()

#Creo un dizionario della squadra
dizionario_squadra = {"portieri": [],
"difensori": [],
"centrocampisti": [],
"attaccanti": []}

#Gestisco i portieri
portieri = 3
budget_portieri = 20
while budget_portieri > 0:
    migliore = max(lista_portieri)
    if migliore[0] > budget_portieri - (portieri - 1):
        lista_portieri.remove(migliore)
    else:
        dizionario_squadra["portieri"].append(migliore)
        portieri -= 1
        lista_portieri.remove(migliore)
        budget_portieri -= migliore[0]

#Gestisco i difensori
difensori = 8
budget_difensori = 40
while budget_difensori > 0:
    migliore = max(lista_difensori)
    if migliore[0] > budget_difensori - (difensori - 1):
        lista_difensori.remove(migliore)
    else:
        dizionario_squadra["difensori"].append(migliore)
        difensori -= 1
        lista_difensori.remove(migliore)
        budget_difensori -= migliore[0]

#Gestisco i centrocampisti
centrocampisti = 8
budget_centrocampisti = 80
while budget_centrocampisti > 0:
    migliore = max(lista_centrocampisti)
    if migliore[0] > budget_centrocampisti - (centrocampisti - 1):
        lista_centrocampisti.remove(migliore)
    else:
        dizionario_squadra["centrocampisti"].append(migliore)
        centrocampisti -= 1
        lista_centrocampisti.remove(migliore)
        budget_centrocampisti -= migliore[0]

#Gestisco gli attaccanti
attacanti = 6
budget_attaccanti = 120
while budget_attaccanti > 0:
    migliore = max(lista_attacanti)
    if migliore[0] > budget_attaccanti - (attacanti - 1):
        lista_attacanti.remove(migliore)
    else:
        dizionario_squadra["attaccanti"].append(migliore)
        attacanti -= 1
        lista_attacanti.remove(migliore)
        budget_attaccanti -= migliore[0]

print("La squadra sarà cosi formata:")

print("Portieri: ", end='')
for i in dizionario_squadra["portieri"]:
    print(f"{i[1]} {i[0]},", end=' ')

print("\n")
print("Difensori: ", end='')
for i in dizionario_squadra["difensori"]:
    print(f"{i[1]} {i[0]},", end=' ')

print("\n")
print("Centrocampisti: ", end='')
for i in dizionario_squadra["centrocampisti"]:
    print(f"{i[1]} {i[0]},", end=' ')

print("\n")
print("Attacanti: ", end='')
for i in dizionario_squadra["attaccanti"]:
    print(f"{i[1]} {i[0]},", end=' ')
