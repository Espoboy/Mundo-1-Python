#Exercício 16: fazer um programa que coleta um numero decimal e transforma em inteiro
from math import trunc
num = float(input('Digite um número decimal:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

#Dá pra fazer sem importar math de duas formas

num2 = float(input('Outro número decimal: '))
print('O valor digitado foi {0} e sua porção inteira é {0:.0f}.'.format(num2))

num3 = float(input('Mais um decimal: '))
print('O valor digitado foi {} e sua porção inteira foi {}.'.format(num3, int(num3)))