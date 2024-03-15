# Ex 33 Ler 3 números e mostrar qual o maior e o menor

num = int(input('Primeiro número:'))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

if num > num2 > num3:
    print('O maior é {} e o menor é {}'.format(num, num3))
if num2 > num3 > num:
    print('O maior é {} e o menor é {}'.format(num2, num))
if num3 > num > num2:
    print('O maior é {} e o menor é {}'.format(num3, num2))
if num > num3 > num2:
    print('O maior é {} e o menor é {}'.format(num, num2))
if num2 > num > num3:
    print('O maior é {} e o menor é {}'.format(num2, num3))
if num3 > num2 > num:
    print('O maior é {} e o menor é {}'.format(num3, num))
if num == num2 == num3:
    print('Os três são iguais!') 