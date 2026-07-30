#se o input ficar aqui vira um loop infinito :(
while True :
    sex = input("Digite seu sexo (m ou f) : ")

    if sex == "m":
        print("Masculino")
        break
    elif sex == "f":
        print("Feminino")
        break
    else :
        print("opcao invalida parceiro faz dnv ai é f ou m ")