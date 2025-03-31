#Apro il file in lettura
infile = "presenze.csv"
try:
    file = open(infile, "r", encoding="UTF-8")
except FileNotFoundError:
    print(f"\nErrore: il file {infile} non è stato trovato.\n")
    exit(1)
except Exception as e:
    print(f"Errore nell'apertura del file: {e}")
    exit(1)

#Scarto la prima riga
file.readline()

#Creo il dizionario core del codice e ciclo le righe del file
dizionario_comunale = {}
for riga in file:
    #Splitto la riga in una lista temporanea
    riga = riga.rstrip().split(";")

    #Fornisco dei nomi parlanti a tutte le variabili
    nome_cognome = riga[0]
    periodo = riga[1].split("-")
    mese_esame = periodo[1]
    sedute_mensili = int(riga[2])
    netto_mensile = int(riga[3])

    #Aggiungo al dizionario i nomi e le loro performance
    if nome_cognome not in dizionario_comunale:
        dizionario_intermedio = {}
        dizionario_comunale[nome_cognome] = dizionario_intermedio

    if mese_esame not in dizionario_intermedio:
        dizionario_intermedio[mese_esame] = (sedute_mensili, netto_mensile)
    
#Chiudo il file
file.close()

#Modifico il dizionario precedente ed individuo chi non ha lavorato
print(f"\nNon ha mi partecipato al consiglio comunale nell'anno 2023: ", end="")
for nome, presenze in dizionario_comunale.items():
    tot_presenze_anno = 0
    tot_lordo_anno = 0

    for mese, busta_paga in presenze.items():
        tot_presenze_anno += busta_paga[0]
        tot_lordo_anno += busta_paga[1]
    
    media_presenze = tot_presenze_anno / len(presenze)

    if tot_presenze_anno == 0:
        print(f" |{nome}| ", end="")

    dizionario_comunale[nome] = (media_presenze, tot_lordo_anno) 
print()

#Sorto il dizionario in ordine di top performers
dizionario_best_performer = dict(sorted(dizionario_comunale.items(), key=lambda x: x[1][0], reverse=True))

#Stampo a video i migliori
print("\nConsiglieri con più sedute mensili: ")
i = 0
for consigliere, performance in dizionario_best_performer.items():
    i += 1
    if i <= 5:
        print(f"{consigliere:<30} {performance[0]:<10.1f} {performance[1]}")

print()