infile = "ufo_sightings.csv"
file = open(infile, "r", encoding="UTF-8")

#Creo il dizionario per salvare i dati del file
dizionario_avvistamenti = {}
for riga in file:
    #Creo una lista temporanea della riga in esame
    temp_list = riga.rstrip().split(",")
    #Separo e salvo in una tripla le info che mi serviranno
    info_avvistamento = (temp_list[3], int(temp_list[4]), temp_list[5])
    #Aggiungo al dizionario con chiave(nome paese) una lista di triple
    if temp_list[2] not in dizionario_avvistamenti:
        dizionario_avvistamenti[temp_list[2]] = []
    
    dizionario_avvistamenti[temp_list[2]].append(info_avvistamento)

file.close()

numero_magggiore_avvistamenti = 0
durata_maggiore_avvistamento = 0
#Itero il dizionario per trovare quello che mi è richiesto
for stato, avvistamenti in dizionario_avvistamenti.items():
    #Il numero degli avvistamenti in uno stato è = alla lunghezza della lista in questione
    numero_avvistamenti = len(avvistamenti)
    #Se il numero di avvistamenti dello staoto in esame è maggiore di quello che prima lo era
    if numero_avvistamenti > numero_magggiore_avvistamenti:
        #Aggiorno l'attuale record
        numero_magggiore_avvistamenti = numero_avvistamenti
        stato_con_piu_avvistamenti = stato
    
    #Itero gli avvistamenti di uno stato per trovare quello dalla maggiore durata
    for avvistamento in avvistamenti:
        if avvistamento[1] > durata_maggiore_avvistamento:
            #Aggiorno l'attuale record
            durata_maggiore_avvistamento = avvistamento[1]
            forma = avvistamento[0]
            tipologia_avvistamento = avvistamento[2]

#Stampo a video quanto richiesto nella consegna
print(f"Lo stato con il maggior numero di avvistamenti è: {stato_con_piu_avvistamenti} con N° avvistamenti: {numero_magggiore_avvistamenti}")
print(f"Avvistamento con la maggiore durata: {tipologia_avvistamento} (durata: {durata_maggiore_avvistamento} secondi, forma: {forma})")
