pessoas = []
totalidade = 0
mulherunder20 = 0
mediaidadde = 0


quantidade = int(input('Digite a quantidade de pessoas que quer cadastrar: '))

for i in range(quantidade):
    dados = {
        'nome' : str(input('Digite o nome do pessoa: ')),
        'idade' : int(input('Digite a idade do pessoa: ')),
        'sexo' : str(input('Digite o sexo do pessoa: ').upper()), #forcando toda entrada a ser maiuscula pra n quebrar dps
    }
    pessoas.append(dados)

for pessoa in pessoas:
    totalidade = totalidade +  pessoa['idade']
    if pessoa['sexo'] == 'F'and pessoa['idade'] < 20:
        mulherunder20 = mulherunder20 + 1

mediaidade = totalidade / quantidade
print('Media das idades do grupo : {:.2f}'.format (mediaidade))
print('Mulheres com menos de 20 anos :',mulherunder20)