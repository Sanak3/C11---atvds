dadosproduto = []
totalvalor = 0

for i in range(3):
    produto = {
        'nome' : input('Digite o nome do produto :'),
        'preco' : int(input('Digite o preço do produto :')),
        'estoque' : int(input('Digite o quantidade de produtos no estoque :')),
    }
    dadosproduto.append(produto)
    totalvalor =  produto['estoque'] * produto['preco']


for item in dadosproduto:
    totalvalor = item['preco'] * item['estoque']
    print('dados do produto:',dadosproduto)
    print('valor em estoque do produto {} com valor total de estoque de {} doletas'.format(item['nome'], totalvalor))
