infile = "parcoPC.txt"
file = open(infile, "r", encoding="UTF-8")

diizonario_pc = {}
for riga in file:
    pc = riga.rstrip()
    diizonario_pc[pc] = [0, 0]

file.close()

infile = "registrazioni.txt"
file = open(infile, "r", encoding="UTF-8")

for riga in file:
    riga = riga.rstrip().split(":")
    computer = riga[0]
    persona = riga[1]

    if computer in diizonario_pc:
        if diizonario_pc[computer][1] == 0:
            diizonario_pc[computer][0] = persona
            diizonario_pc[computer][1] = 1

        elif diizonario_pc[computer][1] == 1:
            diizonario_pc[computer][0] = 0
            diizonario_pc[computer][1] = 0

file.close()

dizionario_persone = {}
for pc, stato in diizonario_pc.items():
    if diizonario_pc[pc][0] != 0:
        if stato[0] not in dizionario_persone:
            dizionario_persone[stato[0]] = []
        dizionario_persone[stato[0]].append(pc)

print("Elenco dei prestiti in corso:")
for persona, pc in dizionario_persone.items():
    print(f"{persona}: {', '.join(pc)}")

print("\nPC disponibili per il prestito:", end="")
for pc, stato in diizonario_pc.items():
    if diizonario_pc[pc][0] == 0:
        print(f" {pc}", end="")
print("\n")




