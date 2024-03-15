# Ex 25 ler um nome de uma pessoa e dizer se ela tem Silva no nome 

nome = str(input('Digite seu nome completo: ')).strip()

print('SILVA' in nome.upper())