import numpy as np

nomes1 = np.array(['julia de sata', 'igor de Deus', 'juba do leste', 'bruninha'])
nomes2 = np.array(['bia', 'arthur', 'samile dos gaviao', 'samuca da pedra'])

concatenados = np.concatenate((nomes1, nomes2))
print('array concatenado:', concatenados)

matriz = concatenados.reshape(2, 4)
print('\narray 2-d (2 linhas x 4 colunas):\n', matriz)

ordenado = np.sort(matriz, axis=None)
invertido = ordenado[::-1]
matriz_decrescente = invertido.reshape(2, 4)
print('\narray 2-d ordenado em ordem decrescente:\n', matriz_decrescente)
