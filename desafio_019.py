import random
nome1 = str(input('Primeiro aluno'))
nome2 = str(input('Segundo aluno'))
nome3 = str(input('Terceiro aluno'))
nome4 = str(input('Quarto aluno'))
lista = [nome1, nome2, nome3, nome4]
sorteado = random.choice(lista)
print('O aluno sorteado foi {}.'.format(sorteado))