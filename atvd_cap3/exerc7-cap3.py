BolaoDosCria = ['farinha','zovo','manteiga','acucar','fermento','leite']
pessoa1 = {'farinha','zovo'}
pessoa2 = {'acucar','fermento'}

print('ingredientes para o bolo :', BolaoDosCria)

PraFazerOBolaoDosCria = set(BolaoDosCria)
ingredientesquetem = pessoa1 | pessoa2
print('ingredientes que tem em :',ingredientesquetem)
OqueFaltaProBolao = PraFazerOBolaoDosCria - ingredientesquetem
print('ingredientes que faltam :',OqueFaltaProBolao)