frase = 'Curso em Vídeo Python'

'''C u r s o   e m   V í  d  e  o     P  y  t  h  o  n'''
'''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'''
'''Lembrando, de 0 a 20 são 21 caracteres.'''

'''Podemos dividir a string criando splits entre os espaços
utilizando o .split() e na visão do programa ficaria assim:'''

'''C u r s o   e m   V í d e o   P y t h o n'''
'''0 1 2 3 4   0 1   0 1 2 3 4   0 1 2 3 4 5  '''
'''____0____   _1_   ____2____   _____3_____ '''

'''Cada palavra irá se tornar uma lista diferente, tendo sua própria
numeração.'''

print('Frase dividida = ', frase.split())

'''Posso reutilizar qualquer string da lista: '''
dividida = frase.split()
print(dividida[0])
print(dividida[0].count('o'))
print(dividida[0] [4])

'''Tendo uma string dividida, podemos usar o ''.join() para adicionar algo
entre cada string única gerada, por exemplo:'''

print('Frase utilizando "-".join = {}'.format('-'.join(frase.split())))
