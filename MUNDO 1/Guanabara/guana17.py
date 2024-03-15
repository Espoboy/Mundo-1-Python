#Ex 15 Aluguel de carros, para cada dia R$60 e cada km R$0.15

dias = int(input('Quantos dias passou com o veículo?\n'))
km = float(input('Quantos km rodados?\n'))
preço = (60 * dias) + (0.15 * km)
print('O valor total a ser pago é de R${:.2f}.'.format(preço))