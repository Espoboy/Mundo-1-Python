#Ex 14 Conversor de Temperaturas, C° em F°

temp = float(input('Digite a temperatura em C°:'))
print('{:.1f} graus Celsius corresponde a {:.1f} Fahrenheit.'.format(temp, ((temp * 1.8) + 32)))