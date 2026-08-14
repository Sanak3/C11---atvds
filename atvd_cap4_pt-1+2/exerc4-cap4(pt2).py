import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
linhas, colunas = matriz.shape

print('Matriz 3x3')

total = linhas * colunas
print('Total dos elementos :',total)

if total % 2 == 0 :
    print('a matriz pode se tornar um vetoe unidimenisonal par')
else:
    print('a matriz pode se tornar um vetoe unidimenisonal impar')