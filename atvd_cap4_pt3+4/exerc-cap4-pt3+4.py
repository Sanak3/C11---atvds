import numpy as np

dados = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

sucesso = dados[1:, 7] == 'Success'
porcentagem = (np.sum(sucesso) / len(sucesso)) * 100
print(f'Porcentagem de missoes que deram certo: {porcentagem:.2f}%')

custos = dados[1:, 6].astype(float)
custos_positivos = custos[custos > 0]
media_gastos = custos_positivos.mean()
print(f'Media de gastos: {media_gastos:.2f}')

localizacoes = dados[1:, 2]
missoes_eua = np.char.find(localizacoes, 'USA') != -1
total_eua = np.sum(missoes_eua)
print('Missoes realizadas pelos EUA:', total_eua)

spacex = dados[dados[:, 1] == 'SpaceX']
custos_spacex = spacex[:, 6].astype(float)
mais_cara = spacex[np.argmax(custos_spacex)]
print('Missao mais cara da SpaceX:', mais_cara[4])
print('Maior custo da SpaceX:', np.max(custos_spacex))

empresas, qtd = np.unique(dados[1:, 1], return_counts=True)
for empresa, total in zip(empresas, qtd):
    print(f'{empresa}: {total}')

retired = dados[1:, 5] == 'StatusRetired'
porcentagem_retired = (np.sum(retired) / len(retired)) * 100
print(f'Porcentagem de foguetes aposentados: {porcentagem_retired:.2f}%')

missoes_russia = np.char.find(localizacoes, 'Russia') != -1
total_russia = np.sum(missoes_russia)
print('Missoes lancadas a partir da Russia:', total_russia)

indice_mais_cara_geral = np.argmax(custos)
empresa_mais_cara = dados[1:][indice_mais_cara_geral, 1]
valor_mais_caro = custos[indice_mais_cara_geral]
print('Empresa da missao mais cara:', empresa_mais_cara)
print('Valor da missao mais cara:', valor_mais_caro)

