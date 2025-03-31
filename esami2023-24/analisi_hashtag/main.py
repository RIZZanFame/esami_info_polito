infile = "hashtags.csv"
file = open(infile, "r", encoding="UTF-8")

dizionario_giorn01 = {}
dizionario_giorn02 = {}
for riga in file:
    temp_list = riga.rstrip().split(" ")
    #splitto la data e controllo il griono
    data_lunga = temp_list[0].split("-")
    data = data_lunga[2]
    lista_hashtag = temp_list[2:]
    if data == "01":
        for hashtag in lista_hashtag:
            if hashtag not in dizionario_giorn01:
                dizionario_giorn01[hashtag] = 1
            else:
                dizionario_giorn01[hashtag] += 1
    else:
        for hashtag in lista_hashtag:
            if hashtag not in dizionario_giorn02:
                dizionario_giorn02[hashtag] = 1
            else:
                dizionario_giorn02[hashtag] += 1

file.close()

dizionario_incremento =  {}
for hastag1, numero1 in dizionario_giorn01.items():
    for hastag2, numero2 in dizionario_giorn02.items():
        if hastag1 == hastag2:
            percentuale_incremento = ((numero2-numero1)/numero1) * 100
            if percentuale_incremento >= 50:
                dizionario_incremento[hastag1] = percentuale_incremento

print("hashtags di tendenza:")

for hashtag, percentuale in dizionario_incremento.items():
    print(f"{hashtag} con un incremento del {percentuale:.0f}%")