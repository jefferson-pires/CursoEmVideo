preco = float(input('Digite o preço do produto: '))
porcentagem_desconto = float(input('Digite a porcetagem de desconto: '))
desconto = preco * (porcentagem_desconto/100)

novo_preco = preco - desconto

print('O valor do desconto é {:.2f} R$'. format(desconto))
print('O novo preço é {} R$'.format(novo_preco))