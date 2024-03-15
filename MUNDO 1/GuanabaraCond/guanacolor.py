# '''Padrão ANSI, utilizado em escala internacional, é um padrão de escape sequences, onde o o caractere
# de escape é a \. Um dos códigos que funcionam melhor pra python é
# \033['código'm. '''

'''Entre o [ e o m podemos ter 1, 2, 3 ou nenhum código'''

'''Abaixo vemos um exemplo com três códigos onde o primeiro é o 
style/estilo do terminal, o 2o é o text/texto e o último é o
background/fundo do texto. A ordem não importa'''

#  \033[0;33;44m

'''No python, os estilos que funcionam melhor no terminal são o 0,1,4 e 7. O 0 é normal,
1 é negrito, 4 é sublinhado e 7 é com o bg invertido'''

'''Nos números de texto, temos de 30 até o 37 que temos as cores:
cinza - 30 | vermelho - 31 | verde - 32 | amarelo - 33 |
azul - 34 | roxo - 35 | ciano - 36 | branco - 37'''

'''Na opção de back ground temos de 40 a 47 na mesma ordem de cores.'''

print('\033[mOlá, mundo!')
print(' ')

a = 5
b = 4

print('Os valores são \033[1;32m{}\033[m e \033[34m{}\033[m!!!'.format(a, b))

# Posso fazer da seguinte maneira também

print('Os valores são {}{}{} e {}{}{}!!!'.format('\033[4;34m', a, '\033[m', '\033[35m', b, '\033[m'))

# E pra finalizar

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'}

print('Os valores são {}{}{} e {}{}{}!!!'.format(cores['azul'], a, cores['limpa'], cores['amarelo'], b, cores['limpa']))

