palavra = input("digite uma palavra: ")
cont = len(palavra)
contletra = 0

for cont in range(cont):
    letraaaa = palavra.upper()[cont]
    print(letraaaa)

    if letraaaa in "AEIOU":
        contletra = contletra+1

print("quantidade de vogais : " , contletra)

if 'A' in  palavra.upper():
    print("contem a letra A")
else :
    print("nao contem a letra A")
