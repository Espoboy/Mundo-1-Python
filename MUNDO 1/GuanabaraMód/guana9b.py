frase = 'Curso em Vídeo Python'

'''C u r s o   e m   V í  d  e  o     P  y  t  h  o  n'''
'''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'''
'''Lembrando, de 0 a 20 são 21 caracteres.'''

'''Podemos utiliza o .replace() para substituir/reposicionar
palavras como por exemplo'''

print('Antes era {}'.format(frase))
print('Com o .replace("Python", "Android") fica {}'.format(frase.replace('Python', 'Android')))

print(' ')

'''O .upper() deixa uma string maiúscula, o .lower() deixa minúscula,
.capitalize() deixa só a primeira letra maiúscula, .title() deixa a primeira
letra de cada palavra da string maiúscula. Segue o exemplo: '''

print('frase.upper() = {}'.format(frase.upper()))
print('frase.lower() = {}'.format(frase.lower()))
print('frase.capitalize() = {}'.format(frase.capitalize()))
print('frase.title() = {}'.format(frase.title()))
print(' ')

frase2 = '   Aprenda Python  '
# As # são espaços
'''# # # A p r e n d a    P  y  t  h  o  n  #  #'''
'''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18'''
'''Lembrando, de 0 a 18 são 19 caracteres.'''

print(frase2)

'''Temos o .strip() que tira os espaços inúteis de uma string,
o .rstip() tira os espaços do lado direito (r de right), temos o
.lstrip() que seguindo a mesma lógica, tira os espaços da esquerda(left)'''
print('.strip() abaixo')
print(frase2.strip())
print('.rstrip() abaixo')
print(frase2.rstrip())
print('.lstrip() abaixo')
print(frase2.lstrip())