#Ex 11 pintando parede, para cada 2m² precisa de 1l de tinta

largura = float(input('Digite a largura da parede: '))
altura = float(input('Agora a altura: '))

area = largura * altura
tinta = area / 2
print('A área da parede equivale a {:.2f}m²'.format(area), end=' ')
print('e será preciso {:.2f} litros de tinta para a pintura.'.format(tinta))