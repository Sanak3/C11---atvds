import pandas as pd

# parte 3
# questao 1
dfPaises = pd.read_csv('paises.csv', delimiter=';')

# 1.a
paises_oceania = dfPaises[dfPaises['Region'].str.contains('OCEANIA')]
print('paises da oceania:\n', paises_oceania['Country'])

# 1.b
print('quantidade de paises da oceania:', len(paises_oceania))

# questao 2
maior_populacao = dfPaises[dfPaises['Population'] == dfPaises['Population'].max()]
print('pais com maior populacao:\n', maior_populacao[['Country', 'Region']])

# questao 3
group_region = dfPaises.groupby('Region')
print('media de alfabetizacao por regiao:\n', group_region['Literacy (%)'].mean())

# questao 4
sem_costa = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]['Country']
sem_costa.to_csv('noCoast.csv', sep=';')

# questao 5
def ajuda_humanitaria(deathrate):
    if deathrate < 9:
        return 'Balanced'
    else:
        return 'Urgent'

dfPaises['Humanitarian Help'] = dfPaises['Deathrate'].apply(ajuda_humanitaria)
print(dfPaises)

# parte 4
# questao 6
group_region = dfPaises.groupby('Region')
estatisticas_pop = group_region['Population'].describe()
print(estatisticas_pop.head(5))

# questao 7
def reduzir_15(valor):
    return valor * 0.85

infant_mortality_orig = dfPaises['Infant mortality (per 1000 births)']
infant_mortality_reduzida = dfPaises['Infant mortality (per 1000 births)'].apply(reduzir_15)
comparacao = pd.concat([infant_mortality_orig, infant_mortality_reduzida], axis=1)
print(comparacao)

# questao 8
dfPaises_sem_coastline = dfPaises.drop('Coastline (coast/area ratio)', axis=1)
dfPaises_sem_coastline.to_csv('paises_sem_coastline.csv', sep=';')
