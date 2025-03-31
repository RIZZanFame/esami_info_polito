from csv import reader, writer

infile = "auto.csv"
auto = open(infile, "r")
csvReader = reader(auto)

categoria_giorni = input("Scegli categoria e giorni: ")
split_stringa = categoria_giorni.split(" ")
categoria = split_stringa[0]
giorni = split_stringa[1:]

for i, giorno in enumerate(giorni):
    giorno = int(giorno)
    giorni[i] = giorno

if len(giorni) > 7:
    print(f"Coglione i giorni della settimana sono 7 non {len(giorni)}")
    categoria_giorni = input("Scegli categoria e giorni: ")

for riga in csvReader:
    if riga[0] == categoria:
        settimana = riga[4:]
        for giorno in giorni:
            disponibile = False
            for i, stato in enumerate(settimana):          
                if giorno - 1 == i and stato == "L":
                    disponibile = True
        if disponibile:
            print(f"{riga[1]} {riga[2]} colore {riga[3]}")
        else:
            print("Macchina non disponibile")
                
                            