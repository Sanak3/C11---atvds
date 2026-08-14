import numpy as np

arr1 = np.ones (8)
arr2 = np.random.randint(0,10,8)

arr3 = arr1 + arr2

total = arr3.sum()

if total >= 40 :
    matriz = arr3.reshape(2,4)
else :
    matriz  = arr3.reshape(4,2)

print('array finale :',arr3)
print('soma total :',total)
print('matriz :\n',matriz)
