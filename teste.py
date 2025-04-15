arq = open(r'C:\Users\mathe\OneDrive\Área de Trabalho\Estágio\Python Data Structures - University of Michigan\Once upon a time, in a cozy little.txt')
#second = arq.read()

for line in arq: # Para cada linha em linha
    line = line.rstrip() # Linha é igual a linha do nosso for com rstrip, tirando linhas e espaços amais de nosso texto
    if line.startswith('But'): # Se a linha começa com 'The', print linha.
        continue

print(line) 


