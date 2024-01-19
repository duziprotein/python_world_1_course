print('-=-'*20)
print('Tente adivinhar o número que pensei!')
import random
n1 = random.randint(0, 5)
num = int(input('Digite um número inteiro entre 0 e 5:'))
if num == n1:
    print('Parabéns, você acertou na mosca!')
else:
    print('Você errou, tente outra vez!')