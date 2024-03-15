# Ex 35 Ler o tamanho de 3 segmentos de reta e descobrir se dá pra montar um triângulo.

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg3 + seg1 > seg2 and seg1 + seg3 > seg2:
    print('\033[34mDÁ\033[m pra formar um triângulo!')
else:
    print('\033[33mNÃO\033[m dá pra formar um triângulo!')