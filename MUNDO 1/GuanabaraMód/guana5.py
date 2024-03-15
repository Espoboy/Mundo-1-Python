# Ex 18 ler um ângulo e mostrar, seno, cosseno e tangente do mesmo.

from math import tan, cos, sin, radians

angulo = float(input('Digite um ângulo: '))

# Transformo em radiano pois os códigos de math esperam que o usuário utilize medidas em radiano

angulo_radiano = radians(angulo)
print('O seno do ângulo de {} é {:.2f}'.format(angulo, sin(angulo_radiano)))
print('O cosseno do ângulo de {} é {:.2f}'.format(angulo, cos(angulo_radiano)))
print('A tangente do ângulo de {} é {:.2f}'.format(angulo, tan(angulo_radiano)))
