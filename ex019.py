from random import choice

aluno1 = input('Digite o nome do 1º aluno: ')
aluno2 = input('Digite o nome do 2º aluno: ')
aluno3 = input('Digite o nome do 3º aluno: ')
aluno4 = input('Digite o nome do 4º aluno: ')

alunos = [aluno1,aluno2,aluno3,aluno4]

sorteado = choice(alunos)

print('\n{} foi o aluno sorteado'. format(sorteado))