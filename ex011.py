altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area_quadrada = altura * largura

quantidade_tinta= area_quadrada / 2

print('\nA area da sua parede é de {} m²'.format(area_quadrada))
print('{} L é a quantidade necessaria para pintar a parede'. format(quantidade_tinta))