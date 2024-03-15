'''TODO COMANDO segue uma sequencia de cima a baixo e da esquerda
para a direita'''

'''Para os operadores condicionais, começaremos com o se e o senão,
if e else. Funcionam da seguinte forma, SE uma condição for satisfeita,
um bloco de códigos irá ser executado, SENÃO será outra sequencia de
códigos. O código submetido às condições deve estar identado, ou seja,
separado por um tab(ou quatro espaços) da 'Parede' do código.
Por exemplo: '''


print('=' * 5, ' BEM VINDO ', '=' * 5)

tempo = int(input('Quantos anos tem seu carro?\n'))

if tempo <= 3:
    print('Tá novinho rapaiz :)')
else:
    print('Tá veinho o coitchado...')


print('=' * 5, ' FIM ', '=' * 5)

print(' ')

#Posso usar as condições da seguinte maneira também:

print('=' * 5, ' BEM VINDO ', '=' * 5)

tempo = int(input('Quantos anos tem seu carro?\n'))

print('Carro novo' if tempo <= 3 else 'Carro Velho')

print('=' * 5, ' FIM ', '=' * 5)

