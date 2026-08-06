pessoas = []
gordao = 0
nomedogordao = ''


for n in range (3):
    dados = {
        'nome': input('Nome: '),
        'peso': int(input('Peso: ')),
    }
    pessoas.append(dados)

magrelo = pessoas[0]['peso']
nomedomagrelo = pessoas[0]['nome']

for n in pessoas:
    if n['peso'] > gordao:
        gordao = n['peso']
        nomedogordao = n['nome']



    if  n['peso'] < magrelo:
        magrelo = n['peso']
        nomedomagrelo = n['nome']

print('pessoa mais pesada :',nomedogordao)
print('pessoa mais leve :',nomedomagrelo)

