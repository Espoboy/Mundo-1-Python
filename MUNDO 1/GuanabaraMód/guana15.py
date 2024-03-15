# Ex 27 ler o nome de uma pessoa e mostrar o primeiro e o último nome.

nome = input('Digite seu nome completo: ').strip()
lista = nome.split()
print('Primeiro nome: {}'.format(lista[0]))
print('Último: {}'.format(lista[len(lista) - 1]))
