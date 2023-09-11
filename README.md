# lidando-com-sequencias-biologicas

## 🧭 Funções

- **gerando-individuo1:** Responsável por correr por uma base de genes, selecionar a quantidade desejável de sequências aleatórias por gene para formar um arquivo fasta de um indivíduo virtual.

- **contagem_frequencia_sequencias:** Faz a leitura de arquivos txt/fasta, separando sequências biológicas e checando a frequência de cada sequência alvo dentro da amostra.

- **illumina_auto, bwa-auto e mpile_auto:** Responsáveis por automatizar processos do art-illumina, bwa e samtools de forma que consigam interagir com o terminal.

- **leitor e media:** Fazem a leitura de arquivos mpileup.txt e conseguem retornar um arquivo txt seguindo a formatação Posição/Gene/Frequência Observada. O *Leitor* separa os reads e sua contagem, *Media* realiza a média da frequência desses reads.



## 👾 Ordem recomendada 
- gerando-individuo1
- contagem_frequencia_sequencias
- illumina_auto
- bwa-auto
- mpile_auto
- leitor
- media
