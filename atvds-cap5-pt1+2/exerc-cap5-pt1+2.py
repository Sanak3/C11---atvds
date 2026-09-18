import numpy as np
import pandas as pd

# parte 1
# questao 1
series_ano1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
series_ano2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

# questao 2
soma_ano1 = series_ano1.sum()
soma_ano2 = series_ano2.sum()
print(f'soma ano 1 = {soma_ano1}')
print(f'soma ano 2 = {soma_ano2}')

# questao 3
crescimento = series_ano2 - series_ano1
print('crescimento de cada linguagem:\n', crescimento)

# questao 4
crescimento_positivo = crescimento[crescimento > 0]
print('linguagens com crescimento positivo:\n', crescimento_positivo)

# questao 5
previsao_ano4 = series_ano2 + (crescimento * 2)
mais_popular = previsao_ano4.nlargest(1)
print('linguagem mais popular no ano 4:\n', mais_popular)

# parte 2
# questao 6
np.random.seed(10)
df = pd.DataFrame(data=np.random.randint(1, 50, [5, 4]), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])
coluna_x = df['X']
x_menor_30 = coluna_x[coluna_x < 30]
media_x = x_menor_30.mean()
print(f'media coluna x menor que 30 = {media_x}')

# questao 7
media_linha_d = df.loc['D'].mean()
soma_linha_e = df.iloc[4].sum()
print(f'media da linha d = {media_linha_d}')
print(f'soma da linha e = {soma_linha_e}')

# questao 8
fatiamento = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print('fatiamento:\n', fatiamento)
print('soma das linhas:\n', fatiamento.sum(axis=1))
print('soma das colunas:\n', fatiamento.sum(axis=0))