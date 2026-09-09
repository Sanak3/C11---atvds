import numpy as np

colors = [
    {"color": "black", "type": "primary", "code": {"rgba": [255, 255, 255, 1], "hex": "#000"}},
    {"color": "green", "type": "secondary", "code": {"rgba": [0, 255, 0, 0.1], "hex": "#0F0"}},
    {"color": "yellow", "type": "primary", "code": {"rgba": [255, 255, 0, 0.7], "hex": "#FF0"}},
    {"color": "blue", "type": "primary", "code": {"rgba": [0, 0, 255, 1], "hex": "#00F"}}
]

print("cores primarias:")
for c in colors:
    if c['type'] == 'primary':
        print(c['color'])

print("\ncodigos hexadecimais com tom de azul maximo:")
for c in colors:
    if c['code']['rgba'][2] == 255:
        print(c['code']['hex'])

elementos = []
for c in colors:
    elementos.append(c['color'])
    elementos.append(c['code']['hex'])

array_1d = np.array(elementos)
print("\narray 1-d:")
print(array_1d)

array_2d = array_1d.reshape(4, 2)
print("\narray 2-d:")
print(array_2d)

array_2d = array_2d.astype(object)
array_2d[array_2d == 'black'] = 'preto'
array_2d[array_2d == 'green'] = 'verde'
array_2d[array_2d == 'yellow'] = 'amarelo'
array_2d[array_2d == 'blue'] = 'azul'

print("\narray 2-d com nomes em portugues:")
print(array_2d)
