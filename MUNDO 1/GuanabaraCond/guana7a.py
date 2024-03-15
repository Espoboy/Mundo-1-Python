# Ex 33 Ler 3 números e mostrar qual o maior e o menor

#MÉTODO GUANABARA

a = int(input('Primeiro número:'))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior é {} e o menor é {}'.format(maior, menor))