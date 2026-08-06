times = ['mengao the best','vasco','sao bambi', 'sem mundial', 'barcelona']

#letra A
print('Primeiros colocados')
for n in times[0:3]:
    print(n)

#letra B
print('Ultimos colocados')
for n in times[3:5]:
    print(n)

#letra C
print('Ordem alfabetica :',sorted(times))

#letra D
for n in times:
    if n == 'barcelona':
        print(times.index(n)+1) #assumindo que o leitor n vai ler o 0 como posicao real da tabela