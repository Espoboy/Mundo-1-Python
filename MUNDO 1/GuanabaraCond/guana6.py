# Ex 32 Ler se um ano é bissexto

from datetime import date

ano = int(input('Digite um ano e se quiser o atual, basta digitar 0: '))

if ano == 0:
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é bissexto!'.format(ano))