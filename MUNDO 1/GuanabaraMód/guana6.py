# Ex 19 Professor quer sortear um de seus 4 alunos

from random import choice

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Segundo: ')
a3 = input('Terceiro: ')
a4 = input('Último aluno: ')

# random.choice escolhe um dos itens da lista

alunos = [a1, a2, a3, a4]
escolhido = choice(alunos)
print('O Aluno escolhido foi {}.'.format(escolhido))