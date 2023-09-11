import os, sys

pasta = input('insira o caminho para a pasta base:')
chr_ref = input('insira o chromossomo ex(chr12):')
intervalo = input('insira o intervalo (ex: xxxxxxxx-xxxxxxxx):')
saida = input('insira o caminho de saida:')

for diretorio, subpastas, arquivos in os.walk(pasta):
	for arquivo in arquivos:
		if 'bam.bai' in arquivo:#supondo que os arquivos .bam.bai e .bam estão na mesma pasta -> utiliza apenas aqueles .bam, pulando .bam.bai
			continue
		nome = diretorio + '/'+ arquivo
		bnome = os.path.basename(nome)
		snome = bnome.replace('bam', 'mpileup.txt')
		cmd = 'samtools mpileup -r '+ chr_ref + ':' + intervalo + ' -a --output-QNAME ' + nome + ' > ' + saida + snome
		print(cmd)
		os.system(cmd)

