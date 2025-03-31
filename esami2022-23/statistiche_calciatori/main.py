infile = "player_stats.csv"
file = open(infile, "r", encoding="UTF-8")
file.readline()

dict_età = {}
dict_centrocampisti = {}
dict_attaccanti = {}

for riga in file:
    #Gestisco il diizonario per l'età
    riga = riga.rstrip().split(",")
    età = 2023 - int(riga[3])
    nome = riga[0]
    assit = float(riga[6])
    minuti = float(riga[4])
    if riga[2] not in dict_età:
        dict_età[riga[2]] = []
    dict_età[riga[2]].append(età)

    #Gestisco il dizionario per i centrocampisti
    if riga[1] == "MF":
        palle_intercettate = float(riga[9])
        palle_recuperate = float(riga[12])
        cross = float(riga[9])
        if cross == 0:
            variabile = 0
        else:
            variabile = assit / cross
        
        efficenza_centr = ((palle_intercettate + palle_recuperate) + variabile) / minuti
        if riga[2] not in dict_centrocampisti:
            dict_centrocampisti[riga[2]] = []
        dict_centrocampisti[riga[2]].append((nome, efficenza_centr))

    #Gestisco il dizionario degli attaccanti
    if riga[1] == "FW":
        goal = float(riga[6])
        fuorigioco = float(riga[7])

        efficenza_att = ((goal + assit - fuorigioco) / minuti)
        if riga[2] not in dict_attaccanti:
            dict_attaccanti[riga[2]] = []
        dict_attaccanti[riga[2]].append((nome, efficenza_att))

file.close()

for nazione, età in dict_età.items():
    tot_età = sum(età)
    età_media = tot_età / len(età)
    dict_età[nazione] = età_media

dict_età_sortato = dict(sorted(dict_età.items(), key=lambda x: x[1]))

for nazione, centrocampisti in dict_centrocampisti.items():
    top_centr_nazione = max(centrocampisti, key=lambda x: x[0][1])
    dict_centrocampisti[nazione] = top_centr_nazione

dict_centrocampisti_sortato = dict(sorted(dict_centrocampisti.items(), key=lambda x: x[1]))
print()