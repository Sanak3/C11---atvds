import numpy as np

dados = np.loadtxt('paises.csv', delimiter=';',dtype=str, encoding='UTF-8')
dados_colunas_iniciais = dados[1: ,0:4]
print(dados_colunas_iniciais)

regioes = dados[1:,1]
regioes_unocas = np.unique(regioes)

print(f'existem {regioes_unocas.size} regioes unicas no world')
for i in regioes_unocas:
    print(i)

alfabet = dados[1:,9].astype(float)
media_alfabet = alfabet.mean()
print(f'media de alfabetizacao {media_alfabet}')

paises_trump = np.char.find(regioes, 'NORTHERN AMERICA') != -1

total_paises_trump = np.sum(paises_trump)

renda = dados[1:, 8].astype(float)
paises = dados[1:, 0]

latinos_indices = np.char.find(regioes, 'LATIN AMER. & CARIB') != -1

renda_latindo = renda[latinos_indices]
paises_latinos = paises[latinos_indices]

indice_maior_renda = np.argmax(renda_latindo)
pais_rico = paises_latinos[indice_maior_renda]
valor_rico = renda_latindo[indice_maior_renda]

print(f'o pais com mair renda do caribe/latino {pais_rico} com renda {valor_rico}')