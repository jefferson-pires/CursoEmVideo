num = float(input('Digite um numero qualquer: '))

decimal = num % 1
inteira = num - decimal

print('o parte inteira do número {} é {}'. format(num, inteira))