from Bio import SeqIO

arquivos = #inserir lista de arquivos gerados por leitor.py 

indv = []
slct_dict = {}

#print('entrando no loop') -> aux checagem 
for arq in arquivos:
    file = open(arq, 'r')
    lines = file.readlines()

    for line in lines:#sequência de slipts
        linha_tab = line.split('\t')
        pos_tab = linha_tab[0]
        gen_tab = linha_tab[1]
        obs_tab = int(linha_tab[2])

        key = pos_tab + '\t' + gen_tab
        old = slct_dict.get(key, 0) 
        slct_dict[key] = obs_tab + old
    #break
f = open('arquivo saida.txt', 'w')#cria arquivo
f.write('Pos\tGene\tn\n')#escreve o cabeçalho

for key in slct_dict:#manda pro arquivo de saída posição, gene e porcertagem 
    old = slct_dict.get(key, 0)/len(arquivos)
    line = key + '\t' + str(old) + '\n'
    f.write(line)
f.close()



