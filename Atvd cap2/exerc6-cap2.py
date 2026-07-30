from numpy.ma.core import sqrt
import math

n = float(input("Digite seu numero : "))
print("raiz : ",sqrt(n))
print("teto : ",math.ceil(n))
print("chao : ",math.floor(n))
print("parte inteira : ",math.trunc(n))

