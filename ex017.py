from math import sqrt

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = sqrt((pow(cateto_adjacente,2) + pow(cateto_oposto,2)))

print('A hipotenusa é igual a {}'. format(hipotenusa))