infile = "penalita.txt"
file = open(infile, "r", encoding="UTF-8")

dizionario_gara = {}
for riga in file:
    riga = riga.rstrip().split(":")
    ID = riga[0]
    penalità = riga[1:]
    streak = 0
    max_streak = 0
    for i, valore in enumerate(penalità):
        penalità[i] = int(valore)
        if int(valore) == 0:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0

    tot_penalità = sum(penalità)
    dizionario_gara[ID] = (tot_penalità, max_streak)

dizionario_classifica = dict(sorted(dizionario_gara.items(), key=lambda x: x[1][0]))
migliore_streak = max(dizionario_gara.items(), key=lambda x: x[1][1])

file.close()

infile = "partecipanti.txt"
file = open(infile, "r", encoding="UTF-8")

dizionario_partecipanti = {}
for riga in file:
    riga = riga.rstrip().split(":")
    ID = riga[0]
    nome = riga[1]
    dizionario_partecipanti[ID] = nome

print("Classifica: ")
for ID, stats in dizionario_classifica.items():
    for pippo, nome in dizionario_partecipanti.items():
        if ID == pippo:
            print(f"{nome} {stats[0]} penalità")
        if pippo == migliore_streak[0]:
            nome_miglior_streaker = nome
    
print(f"\nHa realizzato la più lunga sequenza {nome_miglior_streaker} con {migliore_streak[1][1]} prove consecutive superate senza errori")
print()