# Ex 34 Ler o salário e calcular o aumento, se o salário for > 1250 o aumento será de 10%
#   se for <= 1250 será de 15%

salario = float(input('Digite seu salário: '))

if salario > 1250:
    aumento = salario + (salario * 0.1)
    print('Com um aumento de 10%, seu novo salário é de R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 0.15)
    print('Com um aumento de 15%, seu salário agora é de R${:.2f}'.format(aumento))  