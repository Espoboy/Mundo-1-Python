#Ex 4 dissecando variável, identificando valores

user = input('Digite algo:')

n = user.isnumeric()
l = user.isalpha()
dois = user.isalnum()
m = user.isupper()
mi = user.islower()
de = user.isdecimal()

print('É numérico?', user.isnumeric())
print('É alfabético?', user.isalpha())
print('É alfanumérico?', user.isalnum())
print('É maiúscula?', user.isupper())
print('É minúscula?', user.islower())
print('Está capitalizado?', user.istitle())
