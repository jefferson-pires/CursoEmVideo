salario = float(input('Digite seu salario: R$'))
aumento = salario * (15/100)
novo_salario = salario + aumento

print('O seu aumento foi de R${:.2f}'. format(aumento))
print('Seu salario será R${:.2f}'. format(novo_salario))