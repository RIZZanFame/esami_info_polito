infile = "cfu.dati"
file = open(infile, "r", encoding="UTF-8")

dizionario_CFU = {}
for riga in file:
    riga = riga.rstrip().split(",")
    esame = riga[0]
    CFU = riga[1]
    obbligatorio = riga[2]
    tupla = (CFU, obbligatorio)

    dizionario_CFU[esame] = tupla

file.close()

infile = "esami.log"
file = open(infile, "r", encoding="UTF-8")

dizionario_matricole = {}

for riga in file:
    riga = riga.rstrip().split(",")
    matricola = riga[0]
    corso = riga[2]
    esito = riga[3]

    if esito != "A":
        if int(esito) >= 18:
            if corso in dizionario_CFU:
                CFU = int(dizionario_CFU[corso][0])
                tipologia = dizionario_CFU[corso][1]
                if matricola not in dizionario_matricole:
                    dizionario_matricole[matricola] = []
                
                dizionario_matricole[matricola].append((CFU, tipologia, int(esito)))

file.close()

#0 = non obbligatorio 1 = obbligatorio
for matricola, storico in dizionario_matricole.items():
    tot_voti = 0
    tot_CFU_obl = 0
    tot_CFU_No_obl = 0
    for esiti in storico:
        tot_voti += esiti[2]
        if esiti[1] == "0":
            tot_CFU_No_obl += esiti[0]
        else:
            tot_CFU_obl += esiti[0]
    media_voti = tot_voti / len(storico)
    tot_CFU = tot_CFU_obl + tot_CFU_No_obl
    dizionario_matricole[matricola] = (tot_CFU, tot_CFU_obl, media_voti)

for matricola, storico in dizionario_matricole.items():
    if storico[0] >= 30:
        print(f"Studente {matricola} con {storico[0]} CFU totali e {storico[1]} obbligatori, media voti: {storico[2]:.1f}")
    else:
        print(f"Studente {matricola} con {storico[0]} CFU totali e {storico[1]} obbligatori, anno non passato, media voti: {storico[2]:.1f}")
