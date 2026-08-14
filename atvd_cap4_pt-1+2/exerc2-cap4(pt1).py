import numpy as np

arr1 = np.arange(0,52,2)
arr2 = np.arange(100,49, -2)

print('array 1 :\n',arr1)
print('array2 :\n',arr2)
concat = np.concatenate((arr1,arr2))
print ('array concatenado :',concat)
ord = np.sort(concat)
print ('array ordenado :',ord)

