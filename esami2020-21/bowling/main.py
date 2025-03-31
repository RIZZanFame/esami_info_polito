infile = "bowling.txt"
file = open(infile, "r", encoding="UTF-8")

dict_partita = {}
for riga in file:
    temp_list = riga.rstrip().split(";")
    temp_list_punteggi = temp_list[2:]
    for i in range(len(temp_list_punteggi)):
        temp_list_punteggi[i] = int(temp_list_punteggi[i])
    temp_list_CognomeNome = temp_list[0:2]
    dict_partita[temp_list_CognomeNome[0] + ' ' + temp_list_CognomeNome[1]] = temp_list_punteggi

file.close()

dict_punteggio = {}
for i,val in dict_partita.items():
    punteggio_giocatore = sum(val)
    dict_punteggio[punteggio_giocatore] = i

lista_cresente_punteggio = sorted(dict_punteggio, reverse=True)

for i in lista_cresente_punteggio:
    print(f"{dict_punteggio[i]} = {i}")

for i, val in dict_partita.items():
    counte_strike = 0
    counter_zero = 0
    for numero in val:
        if numero == 10:
            counte_strike += 1
        elif numero == 0:
            counter_zero += 1
    lista_strikeEzero = []
    lista_strikeEzero.append(counte_strike)
    lista_strikeEzero.append(counter_zero)
    dict_partita[i] = lista_strikeEzero

print("")
for i, val in dict_partita.items():
    print(f"{i} ha realizzato {val[0]} Strike e {val[1]} nulle")