infile = "passeggeri.txt"
file = open(infile, "r", encoding="UTF-8")

file.readline()
dizionario_volo = {}
for riga in file:
    temp_list = riga.rstrip().split(",")
    tupla_info_volo = (temp_list[3], temp_list[5])
    tupla_info_passeggero = (temp_list[1], temp_list[2])
    if tupla_info_volo not in dizionario_volo:
        dizionario_volo[tupla_info_volo] = []

    dizionario_volo[tupla_info_volo].append(tupla_info_passeggero)

dizionario_età = {}
numero_massimo = 0
passeggeri_maschi = 0
passeggeri_femmine = 0
for info_volo, passeggeri in dizionario_volo.items():
    età_passeggero = 0
    numero_passeggeri = len(passeggeri)
    for info_passeggero in passeggeri:
        età_passeggero += int(info_passeggero[0])
    media_età = età_passeggero / numero_passeggeri
    dizionario_età[info_volo[0]] = media_età

    if numero_passeggeri > numero_massimo:
        numero_massimo = numero_passeggeri
        volo_più_affolato = info_volo
        if info_passeggero[1] == "M":
            passeggeri_maschi += 1
        elif info_passeggero[1] == "F":
            passeggeri_femmine += 1

print("Media dell'età per ciascuna origine:")
for partenza, età_media in dizionario_età.items():
    print(f"Origine: {partenza}, Media età: {età_media:.1f}")

print(f"\nNumero di volo più popolare: {volo_più_affolato[1]}, paseggeri M: / F: ")
print()