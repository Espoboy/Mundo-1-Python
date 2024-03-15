frase = 'Curso em Vídeo Python'

'''Cada caractere pega um 'microespaço' na memória do pc
onde os espaços também contam. No caso de Curso em vídeo Python são
21 desses microespaços de 0 a 20'''

'''C u r s o   e m   V í  d  e  o     P  y  t  h  o  n'''
'''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'''

'''Se contarmos até o V teremos nove espaços,
se pedirmos para o programa mostrar somente o
espaço de número 9, aparecerá somente o V'''

'''Para isso, usamos a lista [] para pegar um desses
micro espaços da memória'''

print(frase[9])

'''Se utilizarmos ':' o programa vai pegar de um espaço a outro
excluido o último espaço, por exemplo:'''

print(frase[9:13])

'''Esse comando deve pegar do V até o E e não deve aparecer o
espaço de número 13 que é o O'''

'''Se quiser incluir o O é só colocar um número a mais
como por exemplo:'''

print(frase[9:14])

'''Podemos fatiar também com padrões, como dois em dois, três
em três e assim por diante. Para isso, colocamos mais uma vez ':'
e utilizamos outro número, por exemplo'''
# 21 Porque vai até 20, se eu quiser incluir o 20, utilizo 21
print(frase[9:21:2])
# Irá pular de 2 em 2, P y t h o n ficaria P t o, sempre mostrando o segundo
#                      P 1 2 1 2 1

'''Se utilizar somente [:9] é o mesmo que utilizar
[0:9], irá começar do primeiro caractere'''

print(frase[:5])

'''Do mesmo modo, funciona ao contrário
[9:], eu estou pedindo para começar do nove
e seguir até o final da frase'''

print(frase[15:])

'''Na mesma linha de raciocínio temos o [9::3], que começará do cinco
e irá até o fim, porém, pulando de dois em dois'''

print(frase[9::3])
