#Ex 10 Conversor de moedas, R$ em US$

r = float(input('Quantos reais você tem?\n'))
d = r / 3.27
print('Dá pra comprar US${:.2f} com R${:.2f}'.format(d, r))