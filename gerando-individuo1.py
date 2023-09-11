from Bio import SeqIO

arquivos = #coloque seu arquivo ou lista de arquivos aqui

for count in range(5): #no parentese especifique quantas vezes repetir o que se pede abaixo
    indvF = []
    for arq in arquivos: #cria um dicionário com cada arquivo de entrada
        indv_dict = {rec.id : rec.seq for rec in SeqIO.parse(arq, 'fasta')}
        for i in range(2): #puxa 2 sequências aleatórias de cada arquivo 
            import random
            name, id = random.choice(list(indv_dict.items()))
            indvF.append(name + '\n' + str(id) + '\n')
        #print(len(indvF))

    slistF = "".join(map(str, indvF))#tira o colchete e as vírgulas na hora de exportar

    with open('individuo_' + str(count + 1) + '.fasta', 'a') as g: #cria um arquivo 
        for line in str(slistF):
            g.write(line)

