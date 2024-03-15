#Ex 20 agora o professor quer sortear a ordem de apresentação do trabalho entre 4 alunos

from random import shuffle

a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')

#Armazeno em uma lista
alunos = [a1, a2, a3, a4]

#Utilizo o random.shuffle para embaralhar a ordem da lista
print('A ordem dos alunos será a seguinte:')
shuffle(alunos)
print(alunos)