infile = "studenti.csv"
file = open(infile, "r", encoding="UTF-8")

file.readline()

dizionario_studenti = {}
for riga in file:
    riga = riga.rstrip().split(",")
    grado = riga[2]
    tripla = (riga[0], riga[1], riga[3])
    if grado not in dizionario_studenti:
        dizionario_studenti[grado] = []

    dizionario_studenti[grado].append(tripla)

file.close()

infile = "criteria.txt"
file = open(infile, "r", encoding="UTF-8")

lista = file.readlines()
lista_ID = lista[0].rstrip().split(",")
cognome_cercare = lista[1].rstrip()
livello_analiz = lista[2].rstrip()

file.close()

print("\nStudenti trovati per ID: ")
for ID in lista_ID:
    for grado, studenti in dizionario_studenti.items():
        for studente in studenti:
            if studente[0] == ID:
                print(f"ID: {studente[0]}, Cognome: {studente[1]} grado: {grado}, GPA: {studente[2]}")

print("\nStudenti trovati per cognome:")
for grado, studenti in dizionario_studenti.items():
    for studente in studenti:
        if studente[1] == cognome_cercare:
            print(f"ID: {studente[0]}, Cognome: {studente[1]} grado: {grado}, GPA: {studente[2]}")

GPA_tot = 0
for grado, studenti in dizionario_studenti.items():
    if grado == livello_analiz:
        for studente in studenti:
            GPA = float(studente[2])
            GPA_tot += GPA

media = GPA_tot / len(dizionario_studenti[livello_analiz])

print(f"\nMedia del GPA per il grado {livello_analiz}: {media:.2f}\n")