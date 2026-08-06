dados = {}
dados['nome'] = input('Nome: ')
dados['media'] = float(input('Media: '))

if dados['media'] >= 50 :
    print('aprovado')
    dados['situacao'] = 'AP'
else :
    print('reprovado')
    dados['situacao'] = 'REPROVADO'

print(dados)