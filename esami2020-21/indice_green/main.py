infile1 = "population.txt"
infile2 = "animal_plant_count.txt"
file_popolazioni = open(infile1, "r", encoding="UTF-8")
file_ani_pia = open(infile2, "r", encoding="UTF-8")

#Creo il dizionario che ospiterà i dati richiesti
dizionario_complessivo = {}
#Itero entrambi i file assieme, in quanto conscio di avere la stessa nazione per ambo le righe
for riga_pop, riga_ani_pia in zip(file_popolazioni, file_ani_pia):
    #Creo delle liste temporanee che ospitano i dati
    riga_pop = riga_pop.rstrip().split(";")
    riga_ani_pia = riga_ani_pia.rstrip().split(";")

    #Nomino i dati con variabili parlanti
    nazione = riga_pop[0]
    numero_popolazione = int(riga_pop[1])
    numero_animali = int(riga_ani_pia[1])
    numero_piante = int(riga_ani_pia[2])

    #Eseguo i calcoli richiesti
    densità_animali = numero_animali / numero_popolazione
    densità_piante = numero_piante / numero_popolazione
    indice_green = ((densità_animali + densità_piante) / 2) * 100

    #Salvo i dati nel dizionario
    dizionario_complessivo[nazione] = (densità_animali, densità_piante, indice_green)

file_popolazioni.close()
file_ani_pia.close()

#Ordino per massimo i dati richiesti
max_densità_animali = max(dizionario_complessivo.items(), key=lambda x: x[1][0])
max_densità_piante = max(dizionario_complessivo.items(), key=lambda x: x[1][1])

#Creo un nuovo dizionario in ordine di indice green decrescente
dict_ord_indice = dict(sorted(dizionario_complessivo.items(), key=lambda x: x[1][2], reverse=True))

#Stampo a video quanto richeisto
print(f"La nazione con il più alto rapporto di animali per popolazione è {max_densità_animali[0]} con un rapport di {max_densità_animali[1][0]:.3f}")
print(f"La nazione con il più alto rapporto di piante per popolazione è {max_densità_piante[0]} con un rapport di {max_densità_piante[1][1]:.3f}")

#Uso un controllo di "indice" per stampare solo la top 3
indice = 0
print("\nLe prime 3 nazioni in ordine decrescente di Indice Green sono:")
for paese, specifiche in dict_ord_indice.items():
    indice += 1
    if indice < 4:
        print(f"{indice}. {paese} - indice green {specifiche[2]:.2f}")
print()