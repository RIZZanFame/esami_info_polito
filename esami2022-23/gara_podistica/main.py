infile = "atleti.txt"
file = open(infile, "r", encoding="UTF-8")

dizionario_atleti = {}
tot_atleti = 0
for riga in file:
    tot_atleti += 1
    riga = riga.rstrip().split(";")
    codice = riga[0]
    competizione = riga[1]
    tempi = riga[2]
    tempi = list(map(float, tempi.split(",")))
    media_tempi_tot = sum(tempi) / len(tempi)
    media_tempi_ultimi_3_allenamenti = sum(tempi[-3:]) / 3

    info = (codice, media_tempi_tot, media_tempi_ultimi_3_allenamenti)
    
    if competizione not in dizionario_atleti:
        dizionario_atleti[competizione] = []

    dizionario_atleti[competizione].append(info)

dizionario_atleti = dict(sorted(dizionario_atleti.items()))

file.close()

dizionario_statistiche = {}
for tipo, atleti in dizionario_atleti.items():
    tempo_tot = 0
    for i in range(len(atleti)):
        tempo = atleti[i][1]
        tempo_tot += tempo
    media_tempo = tempo_tot / len(atleti)
    dizionario_statistiche[tipo] = media_tempo

scostati = []
scostati_10 = 0
for tipologia, tutti_atleti in dizionario_atleti.items():
    for t, tempo_medio in dizionario_statistiche.items(): 
        atleti_scostati_3 = 0
        for atleta in tutti_atleti:
            scostamento_3 = abs((atleta[2] - tempo_medio) / tempo_medio) * 100
            scostamento_10 = abs((atleta[1] - tempo_medio) / tempo_medio) * 100
            if scostamento_10 < 10:
                scostati_10 += 1
            if scostamento_3 < 3:
                scostati.append(atleta[0])
    print(f"Gli altleti nella tipologia {tipologia} sono: {len(dizionario_atleti[tipologia])}")
    print(f"Gli atleti nel top 3% sono: {', '.join(scostati)}\n")
    scostati = []

print(f"In totale gli atleti selezionati sono {scostati_10} su {tot_atleti} ({((scostati_10/tot_atleti) * 100):.2f}%)")
print()