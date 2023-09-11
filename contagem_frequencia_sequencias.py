arquivo = #[seu arquivo aqui]

file = open(arquivo, 'r')
lines = file.readlines()
upArq = []

for line in lines:#transforma str em caixa alta
    newarq = line.upper()
    upArq.append(newarq)
#print(upArq)

seq = []
for iline in upArq: # lê o arquivo e manda pra variável seq só o que não começa com '>'
    if iline.find('>') != 0:
        seq.append(iline)
#print(seq)

seqDict = {}

for sequencia in seq:#monta um dicionário com chave = sequência/valor = frequência  
    count = seq.count(sequencia)
    seqDict[sequencia] = count/len(seq) #[insira o valor base da frequência]
#print(seqDict)
#print(seqDict.values())

selctList = []
aux = "" #variável auxiliar
count = 1

for sequ, frequ in seqDict.items():#monta uma lista a partir do dicionário apenas com as sequências selecionadas
    if aux != sequ:
        if frequ > 0.01:
            sequ = sequ.rstrip("\n")
            selctList.append(">SEQ_" + str(count) + "\n")
            selctList.append(sequ + "\n")

            count = count + 1
    aux = sequ
print(selctList)
