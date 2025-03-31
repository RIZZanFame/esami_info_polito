infile = "punteggi.txt"
file = open(infile, "r", encoding="UTF-8")

dizionario_atleti = {}
for riga in file:
    temp_list_riga = riga.rstrip().split(" ")
    nome_cognome = temp_list_riga[0] + ' ' + temp_list_riga[1]
    lista_punteggi = temp_list_riga[4:]
    i = 0
    for voto_str in lista_punteggi:
        voto_str = float(voto_str)
        lista_punteggi[i] = voto_str
        i += 1
    punteggio_massimo = max(lista_punteggi)
    lista_punteggi.remove(punteggio_massimo)
    punteggio_minimo = min(lista_punteggi)
    lista_punteggi.remove(punteggio_minimo)
    totale_punteggio = round(sum(lista_punteggi), 2)
    lista_punteggi.append(totale_punteggio)
    dizionario_atleti[(nome_cognome, temp_list_riga[2], temp_list_riga[3])] = lista_punteggi

file.close()

punteggio_ITA = 0
punteggio_USA = 0
punteggio_RUS = 0
punteggio_GRB = 0
for informazione, punteggi in dizionario_atleti.items():
    if informazione[2] == "ITA":
        punteggio = punteggi[3]
        punteggio_ITA += punteggio
    elif informazione[2] == "USA":
        punteggio = punteggi[3]
        punteggio_USA += punteggio
    elif informazione[2] == "RUS":
        punteggio = punteggi[3]
        punteggio_RUS += punteggio
    elif informazione[2] == "GRB":
        punteggio = punteggi[3]
        punteggio_GRB += punteggio

dizionario_classifica = {"Italia": punteggio_ITA,
"Russia": punteggio_RUS,
"Stati Uniti": punteggio_USA,
"Regno Unito": punteggio_GRB}  
classifica = sorted(dizionario_classifica)
print()
        
    