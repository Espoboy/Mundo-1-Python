# Ex 28 Randomizar um número entre 0 e 5 e pedir ao usuário para advinhar

from random import randint
from time import sleep

print('-=-' * 20)
print('Eu pensei em um número entre 0 e 5. \033[35mVocê jamais advinharia!\033[m')
print('-=-' * 20)
num = randint(0,5)
tentativa = int(input('Tente a sorte: '))


print('\033[33mPROCESSANDO...\033[m')
sleep(2)
# Sleep serve para dar uma pausa temporária no andamento do código


if tentativa == num:
    print('Parabéns! O número era {}'.format(num))
else:
    print('\033[32mQuase lá!\033[m O número \033[35mcorreto\033[m era \033[32m{}\033[m'.format(num))