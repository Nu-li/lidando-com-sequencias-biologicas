arquivo = #inserir lista de arquivos mpileup

file = open(arquivo, 'r')
lines = file.readlines()

for line in lines: #faz a quebra da linha no tab
    linha_tab = line.split("\t")
    if linha_tab[3] != "0":
        pos = linha_tab[1]
        reads = linha_tab[6].split(",")

        dict = {}
        for i in reads: #cria um dicionário com gene e sua contagem 
            z = i.split("_")
            gene = z[1]
            dict[gene] = dict.get(gene,0) + 1
        #print(dict)
        
        linhalist = []
        for g in dict: #monta uma linha de posição\gene\contagem e manda pra lista
            linha = pos +'\t' + gene + '\t' + str(dict.get(gene,0)) + '\n'
            linhalist.append(linha)

        with open('reads_indv.txt', 'a') as f: #cria um arquivo 
            for linha in linhalist:
                f.write(linha)
file.close()

