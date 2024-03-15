# Ex 22 Ler  Nome completo de uma pessoa e mostrar com as letras maiusculas, minúsculas
#   Quantas letras sem os espaços  e quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ').strip()
nomes = nome.split()
primeiro_nome = nomes[0]

print('Em maiúsculo: {}'.format(nome.upper()))
print('Em minúsculo: {}'.format(nome.lower()))
print('Tem {} letras.'.format(len(nome) - nome.count(' ')))
print('O primeiro nome {}, tem {} letras.'.format(primeiro_nome, len(primeiro_nome)))
#Posso descobrir o primeiro nome de outra forma, identificando o Primeiro espaço dado

print('O primeiro nome tem {} letras'.format(nome.find(' ')))