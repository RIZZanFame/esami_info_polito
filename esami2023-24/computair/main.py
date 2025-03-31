infile = "flights.txt"
file = open(infile, "r", encoding="UTF-8")

dizionario_voli = {}
for riga in file:
    temp_list = riga.rstrip().split(";")
    dizionario_voli[temp_list[0]] = temp_list[1:]

file.close()

passeg_tot = 0
for code, specifiche in dizionario_voli.items():
    num_passeg = int(specifiche[1])
    passeg_tot += num_passeg

media_passeg = passeg_tot / len(dizionario_voli)
print(f"Numero medio di passeggeri: {media_passeg}")

infile = "weather.txt"
file = open(infile, "r", encoding="UTF-8")

print("\nCodice dei voli verso città con condizione meteorologica Rainy o Stormy:")
for riga in file:
    temp_list = riga.rstrip().split(";")
    if temp_list[1] == "Rainy" or temp_list[1] == "Stormy":
        for code, specifiche in dizionario_voli.items():
            if temp_list[0] == specifiche[0]:
                print(f"* {code} verso: {specifiche[0]}: {temp_list[1]}")

dizionario_aggiornato = {}
for i, volo in dizionario_voli.items():
    if volo [0] not in dizionario_aggiornato:
        dizionario_aggiornato[volo[0]] = int(volo[1])
    else:
        passeggeri = dizionario_aggiornato[volo[0]] + int(volo[1])
        dizionario_aggiornato[volo[0]] = passeggeri

print()
for i, passe in dizionario_aggiornato.items():
    print(f"{i}: {passe} passeggeri in arrivo")
