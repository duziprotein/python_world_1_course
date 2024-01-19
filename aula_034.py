n1 = float(input('Digite o valor do seu sálário em R$:'))
n2 = 10 * n1/100
n3 = 15 * n1/100
n2_2 = n1 + n2
n3_3 = n1 + n3
if n1 > 1250.00:
    print('Seu aumento salarial de 10% foi de R$ {:.2f}, passando a receber R$ {:.2f}.'.format(n2,n2_2))
if n1 <= 1250.00:
    print('Seu aumento salarial de 15% foi de R$ {:.2f}, passando a receber R$ {:.2f}.'.format(n3,n3_3))
