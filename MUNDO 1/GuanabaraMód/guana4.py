#Ex 17 fazer um programa que calcula a hipotenusa de um triângulo rentângulo.
from math import sqrt, hypot

# Importei o sqrt para tirar a raíz, porém posso utilizar o método tradicional
# hip ** (1/2)
# Posso utilizar diretamente também o math.hypot que calcula a hipotenusa

a = float(input('Cateto oposto: '))
b = float(input('Cateto adjacente: '))
hip = pow(a, 2) + b ** 2
c = sqrt(hip)
#c = hypot(a, b)
#c = hip ** (1/2)
print('A partir do cálculo com os valores {} e {} a hipotenusa vale {:.2f}.'.format(a, b, c))