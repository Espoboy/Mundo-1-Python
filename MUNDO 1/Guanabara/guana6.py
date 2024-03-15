#Ex 6 dobro triplo e raíz

n1 = int(input('Um valor:'))
n2 = int(input('Outro:'))

s = n1 + n2
m = n1 * n2
d = n1 / n2
sub = n1 - n2
di = n1 // n2
p = n1 ** n2

# {:.3f} para utilizar somente 3 casas float e \n quebra a linha
print('A soma vale {}, o produto {}, a \ndivisão, {:.3f}'.format(s, m, d), end='')
print(' a divisão inteira {} e potência {}'.format(di, p))