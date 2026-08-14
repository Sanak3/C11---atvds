import numpy as np

np.random.seed(10)

matriz = np.random.randint(1,51, [4,4])
medialinha = matriz.mean(axis=1)
mediacoluna = matriz.mean(axis=0)

print('media dos valores da linah :', medialinha)
print('media dos valores da coluna :',mediacoluna)

bigmedialinha = medialinha.max()
bigmediacoluna = mediacoluna.max()

print('maior media das linhas : ',bigmedialinha)
print('maior media das coluna : ',bigmediacoluna)

elementao, cont = np.unique(matriz, return_counts=True)
print('numeros unicos :',elementao)
print('quatidade de vezes que apareceram : ',cont)

duasvezesapenas = elementao[cont==2]
print('num que aparecem duas vezes : ',duasvezesapenas)
