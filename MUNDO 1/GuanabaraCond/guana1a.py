'''Podemos usar o programa das médias como exemplo de utilidade
para os operadores condicionais.'''

m1 = float(input('Digite sua nota em matemática: '))
p1 = float(input('Digite sua nota em português: '))
media = (m1 + p1) / 2
if media >= 6:
    print('Parabéns, você passou! Sua média foi de {:.1f}'.format(media))
else:
    print('Ano que vem você tenta novamente... Sua média foi de {:.2f}'.format(media))