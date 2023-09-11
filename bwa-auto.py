import os, sys

pasta = input('insira o caminho de entrada:')
gene_ref = input('insira o caminho para o gene de referencia:')

for diretorio, subpastas, arquivos in os.walk(pasta):
	for arquivo in arquivos:
		#print(os.path.join(diretorio, arquivo))
		if not "1.fq" in arquivo: 
			continue

		r1 = diretorio + arquivo
		r2 = r1.replace("1.fq","2.fq")
		
		nome_base = os.path.basename(r1)
		bam = nome_base.replace("_1.fq",".bam")

		cmd = 'bwa mem -t 8 '+ gene_ref + ' ' + r1 + ' ' + r2 + ' | samtools sort - > /home/nome/diretorio/saida/arquivos/bwa/'+ bam
		print(cmd)
		os.system(cmd)
		cmd = 'samtools index /home/nome/diretorio/para os/arquivos/saida_bwa/'+ bam
		print(cmd)
		os.system(cmd)
		#break

