import numpy as np

musicas = []

while True :
    aux = int(input('Deseja adicionar uma musica ? 0 = n e 1 = s : '))
    if aux == 0 :
        break
    else :
            musica = {
                 'nome' : input('Nome do musica: '),
                 'ano' : int(input('Ano de lançamento da musica: ')),
            }
            musicas.append(musica)

print(f'quantidade de musicas em barra : {len(musicas)}')
if musicas :
    musica_antiga = min(m['ano'] for m in musicas)
    print(f'musica mais antiga : {musica_antiga}')
    for m in musicas :
        if m['ano'] == musica_antiga :
            print(f'musica: {m['nome']} e ano : {m['ano']}')