from math import ceil, floor, sqrt

## Posso utilizar somente o import math ou posso escolher o que vou importar utilizando o from
## utilizando o from, eu devo usar somente raiz = sqrt(num)
## sem o from, deve ser math.sqrt(num)
num = int(input('Digite um número:'))
raiz = sqrt(num)
# math.sqrt Square Root
# math.ceil arredondar cima
# math.floor arredondar baixo
print('A raíz de {} é igual a {:.2f}'.format(num, ceil(raiz)))