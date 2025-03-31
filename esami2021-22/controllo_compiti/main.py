infile = "risposte.txt"
risposte = open(infile, "r", encoding="UTF-8")

dizionario_risposte = {}
for riga in risposte:
    temp_list = riga.rstrip().split(" ")
    dizionario_risposte[temp_list[0]] = temp_list[1:]

risposte.close()

infile = "posizioni.txt"
posizioni = open(infile, "r", encoding="UTF-8")

for fila in posizioni:
    lista_fila = fila.rstrip().split(" ")
    for i in range(len(lista_fila)):
        if i != (len(lista_fila) -1) :
            if dizionario_risposte[lista_fila[i]] == dizionario_risposte[lista_fila[i+1]]:
                print(f"Le risposte di {lista_fila[i]} e {lista_fila[i+1]} sono le stesse")
            else:
                ha_copiato = True
                risposta_extra = False
                for uno, due in zip(dizionario_risposte[lista_fila[i]], dizionario_risposte[lista_fila[i+1]]):
                    if uno != "-" and uno != due:
                        ha_copiato = False
                    if uno == '-' and due != '-':
                        risposta_extra = True
                if ha_copiato and risposta_extra:
                    print(f"{lista_fila[i]} potrebbe aver copiato da {lista_fila[i+1]}")