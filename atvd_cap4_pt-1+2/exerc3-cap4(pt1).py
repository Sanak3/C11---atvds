import numpy as np

campao = np.zeros((2,2) , dtype=int)
linhabombom = np.random.randint(0,2)
colunabombom = np.random.randint(0,2)
campao[linhabombom][colunabombom] = 1 #aloca a bomba em coluna e linha aleatoria

venceu = True

for jogadas in range(3):
    linhajogada = int(input('Escolha a linha 0 ou 1 :'))
    colunajogada = int(input('Escolha a coluna 0 ou 1 :'))

    if campao[linhajogada][colunajogada] == 1:
        print('Ta pegando fogo bixo, game over parceiro')
        venceu= False
        break
    else:
        print('Acertou miseravi')

if venceu:
    print('Boa viverá para lutar mais um dia, parabens :p')