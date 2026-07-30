
while True :
    num = int(input("Digite seu numero : "))
    if num < 1000:
        print("o numero tem que ser maior que 1000")

    elif num > 9999:
        print("o numero tem que ser menor que 9999")

    else :
        transformandosapohaemtxt = str(num)
        print ("Unidade : {}".format(transformandosapohaemtxt[3]))
        print ("dezena  : {}".format(transformandosapohaemtxt[2]))
        print ("centena : {}".format(transformandosapohaemtxt[1]))
        print ("milhar : {}".format(transformandosapohaemtxt[0]))
    break