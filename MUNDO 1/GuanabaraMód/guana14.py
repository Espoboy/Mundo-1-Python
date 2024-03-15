# Ex 26 Ler uma frase, dizer quantas vezes aparece letra A, qual posição ela aparece
#   na primeira vez e na última

frase = input('Digite uma Frase: ').strip().upper()


print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A última apareceu na posição {}'.format(frase.rfind('A') + 1))