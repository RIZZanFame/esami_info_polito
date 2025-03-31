infile = "instagram.csv"
file = open(infile, "r", encoding="UTF-8")

dizionario_instagram = {}
top_lunghezza_professione = 0
for riga in file:
    riga = riga.rstrip().split(";")
    professione = riga[3]
    follower = float(riga[2])
    lunghezza_professione = len(professione)
    if lunghezza_professione > top_lunghezza_professione:
        top_lunghezza_professione = lunghezza_professione

    if professione not in dizionario_instagram:
        dizionario_instagram[professione] = []

    dizionario_instagram[professione].append(follower)

file.close()

for prof, follower in dizionario_instagram.items():
    followers = sum(follower)
    dizionario_instagram[prof] = followers

dizionario_ordinato = dict(sorted(dizionario_instagram.items(), key=lambda x: x[1], reverse=True))

print("Migliori professioni per n° di followers:")
for professione, follower in dizionario_ordinato.items():
    print(f"{professione:<{top_lunghezza_professione}} {follower:.1f}")