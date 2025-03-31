infile = "mazzo.txt"
file = open(infile, "r", encoding="UTF-8")

#creo una lista generale del mazzo
mazzo_tot = []
#per ogni riga di mazzo.txt salvo il colore in mazzo totale
for riga in file:
    if riga != "":
        mazzo_tot.append(riga.rstrip())

#stabiisco quante giocate saranno possibili
giocate_tot = len(mazzo_tot) // 2

#per ogni elemento di mazzo_tot salvo alternat. in una e nell'altra lista
mazzo_G1 = []
mazzo_G2 = []
i = 0
for val in mazzo_tot:
    if i % 2 == 0:
        mazzo_G1.append(val)
    if i % 2 == 1:
        mazzo_G2.append(val)
    i += 1

#creo una copia delle due liste che userò per convertire i colori nei valori
mazzo_G1_num = list(mazzo_G1)
mazzo_G2_num = list(mazzo_G2)

#riempo la lista 1 con i rispettivi valori dei colori
j = 0
for val in mazzo_G1_num:
    if val == "Rosso":
        mazzo_G1_num[j] = 5
    if val == "Verde":
        mazzo_G1_num[j] = 3
    if val == "Giallo":
        mazzo_G1_num[j] = 1
    j += 1

#riempo la lista 2 con i rispettivi valori dei colori
j = 0
for val in mazzo_G2_num:
    if val == "Rosso":
        mazzo_G2_num[j] = 5
    if val == "Verde":
        mazzo_G2_num[j] = 3
    if val == "Giallo":
        mazzo_G2_num[j] = 1
    j += 1

#stabilisco chi ha vinto ed il punteggio parziale
punteggio_G1_tot = 0
punteggio_G2_tot = 0
for i in range(0, giocate_tot):
    punteggio_G1 = 0
    punteggio_G2 = 0
    punteggio_pari = 0
    print(f"Mano N°{i+1}")
    print(f"Carta giocatore 1: {mazzo_G1[i]}")
    print(f"Carta giocatore 2: {mazzo_G2[i]}")
    
    if mazzo_G1_num[i] > mazzo_G2_num[i]:
        print("Vince la mano il giocatore 1")
        punteggio_G1 = mazzo_G1_num[i] + mazzo_G2_num[i]
    elif mazzo_G1_num[i] < mazzo_G2_num[i]:
        print("Vince la mano il giocatore 2")
        punteggio_G2 = mazzo_G1_num[i] + mazzo_G2_num[i]
    else:
        print(f"Pareggio")
        punteggio_pari = mazzo_G1_num[i] + mazzo_G2_num[i]
    punteggio_G1_tot = punteggio_G1_tot + punteggio_G1 + punteggio_pari
    punteggio_G2_tot = punteggio_G2_tot + punteggio_G2 + punteggio_pari
    print(f"il punteggio del giocatore 1 è: {punteggio_G1_tot}")
    print(f"il punteggio del giocatore 2 è: {punteggio_G2_tot}")
    print("")
if punteggio_G1_tot > punteggio_G2_tot:
    print(f"Vince la partita il giocatore 1 con un punteggio di: {punteggio_G1_tot}")
elif punteggio_G1_tot < punteggio_G2_tot:
    print(f"Vince la partita il giocatore 2 con un punteggio di: {punteggio_G2_tot}")
 
file.close()