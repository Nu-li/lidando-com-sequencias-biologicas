import os, sys


pasta= input('insira o caminho:')#caminho completo até a pasta com os arquivos 
#print('entrando no loop') aux na checagem
for diretorio, subpastas, arquivos in os.walk(pasta):#caminha pelos arquivos
	for arquivo in arquivos:
		#print(os.path.join(diretorio, arquivo)) -> para checar se o caminho indicado está correto
		caminho = diretorio + arquivo
		nome_base = os.path.basename(caminho)#pega o nome base para quebrar e automatizar a nomeação dos arquivos de saída
		quebra = nome_base.split('.')
		nome = quebra[0]
		saida = 'caminho completo para a pasta de saída' + nome + '_' 
		dados = 'caminho no computador para o art-illumina/art_illumina -ss HS25 -i ' + caminho + ' -p -l parâmetro -f parâmetro -m parâmetro -s parâmetro -na -o ' + saida
		#print(dados) 
		os.system(dados)				
		#break
		
						#parâmetro: insira em seu lugar os parâmetros desejados na variável 'dados'
		
		
		

