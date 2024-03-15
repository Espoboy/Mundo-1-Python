# Ex 29 Ler a velocidade de um carro e se ele ultrapassar 80km/h
#   mostre que ele foi multado por R$7 para cada km/h excedido

v = float(input('Qual a velocidade do carro?\n'))

if v > 80:
    multa = (v - 80) * 7
    print('Ok. Por andar a {}km/h vc foi multado em R${:.2f}'.format(v, multa))

print('Tenha um ótimo dia! Dirija com atenção sempre.')