frase = 'Curso em Vídeo Python'

'''C u r s o   e m   V í  d  e  o     P  y  t  h  o  n'''
'''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'''
'''Lembrando, de 0 a 20 são 21 caracteres.'''

'''Podemos também analisar strings, como por exemplo,
utilizaremos o 'len()', que vem de length(comprimento),
para analisar o comprimento da frase'''

print(' ')

print(frase, 'Tem {} caracteres'.format(len(frase)))

'''Temos também o .count('letra'), que conta quantas vezes
uma certa letra se repete na string.'''

print(' ')

print(frase, 'Tem {} letras O'.format(frase.count('o')))

'''Podemos fatiar e usar o count ao mesmo tempo
utilizando-o da seguinte forma:'''

print(' ')

print("""Do caractere 0 ao 12 da frase {} temos {} letras O""".format(frase, frase.count('o', 0, 13)))
# Lembrando que NÃO INCLUI O 13

'''Podemos também procurar uma certa parte da string
utilizando o comando .find() como mostra o exemplo a seguir.'''

print(' ')

print('Em que caractere começa a parte thon de Python?', frase.find('thon'))

'''O programa deve nos mostrar onde começa o 'thon' na frase
que no nosso caso começa no 17'''

'''Se colocarmos uma string que o programa não encontra
ele nos retorna -1, nos indicando que não encontrou tal string'''

print('Em que caractere começa a palavra Android?', frase.find('Android'))

print(' ')

'''Podemos também verificar se uma string existe através do comando
in, que irá nos retornar True ou False, como por exemplo:'''

print('Existe a palavra Curso na frase?', ('Curso' in frase))
print('Existe a palavra Android na frase?', ('android' in frase))

print(' ')

'''Podemos utilizar aspas duplas " três vezes para um print longo e utilizar
as outras funções normalmente:'''

print("""Olá, mundo! Que prazer é saudar cada canto e recanto
deste vasto planeta que compartilhamos.
De montanhas majestosas a vales serenos,
de oceanos profundos a desertos ardentes,
cada parte de ti é uma maravilha a ser descoberta. 
Bem vindo ao {}""".format(frase))