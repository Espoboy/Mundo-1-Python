# Ex 23 Ler um número de 0 a 9999 e mostre os digitos separados.

numero = int(input('Digite um número: '))

'''u = numero // 1 % 10: Isola o dígito das unidades. Divide o número por 1 para obter o próprio 
número (pois qualquer número dividido por 1 é o próprio número) e, em seguida, usa o operador
de resto % 10 para pegar o último dígito (a unidade).'''

'''d = numero // 10 % 10: Isola o dígito da dezena. O número é dividido 
por 10 para mover o dígito das dezenas para a unidade (10 se torna 1), 
e depois o operador de resto % 10 é usado para obter o último dígito, que agora é a dezena.'''

'''E assim por diante'''

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10 

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))