#Apro il primo file
infile = "viaggi_enterprise.txt"
file = open(infile, "r", encoding="UTF-8")

#Creo il dizionario
dizionario_viaggi = {}

#Nomino i dati per calcolare le future medie
durata_tot_viaggio = 0
num_tot_passeg = 0

#Ciclo il file
for riga in file:
    #Elaboro la riga
    riga = riga.rstrip().split(",")
    #Nomino le variabili con nomi parlanti
    pianeta = riga[0]
    durata = int(riga[1])
    viaggiatori = int(riga[2])

    #Salvo i dati nel diizonario
    dizionario_viaggi[pianeta] = (durata, viaggiatori)

    #Elaboro già le i dati  per calcolare le medie
    durata_tot_viaggio += durata
    num_tot_passeg += viaggiatori

#Calcolo le medie
durata_media = durata_tot_viaggio / len(dizionario_viaggi)

#Stampo a video quanto richiesto
print(f"Durata media dei viaggi: {durata_media}")
print(f"Numero totale di passeggeri: {num_tot_passeg}")

#Chiudo il file
file.close()

#Apro il secondo file
infile = "lingue_pianeti.txt"
file = open(infile, "r", encoding="UTF-8")

dizionario_lingue = {}

print("\nLingue parlate su ciascun pianeta visitato:")
#Ciclo il file
for riga in file:
    #Elaboro la riga
    riga = riga.rstrip().split(",")
    #Nomino le varibili con nomi parlanti
    pianeta = riga[0]
    lingue = riga[1:]
    for lingua in lingue:
        if lingua not in dizionario_lingue:
            dizionario_lingue[lingua] = 1
        else:
            cont_lingue = dizionario_lingue[lingua]
            cont_lingue += 1
            dizionario_lingue[lingua] = cont_lingue

    #Stampo a video quanto richiesto
    if pianeta in dizionario_viaggi:
        print(f"{pianeta}: {lingue}")

#Chiudo il file
file.close()

#Creo una lista ordinata delle lingue top
lista_lingue_top = sorted(dizionario_lingue.items(), key=lambda x: x[1], reverse=True)
lista_lingue_top = lista_lingue_top[:3]
lista_lingue_top = sorted(lista_lingue_top, key=lambda x: x[1])

#Stampo a video le n lingue top richieste
print(f"\nLe tre lingue più ricorrenti tra i pianeti visitati sono: ")
for i in range(len(lista_lingue_top)):
    print(lista_lingue_top[i][0])
