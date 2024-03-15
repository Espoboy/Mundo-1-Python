# Ex 31 Ler a distancia de uma viagem em km cobrando R$0,50 por km
#   se for menos de 200km se for mais R$0,45

km = float(input('Quão longe em km é a cidade que deseja ir?\n'))
if km <= 200:
    preço = km * 0.5
else:
    preço = km * 0.45
print('O valor da viagem será de R${:.2f}'.format(preço))
