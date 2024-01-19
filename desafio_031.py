n1 = float(input('Quantos quilomêtros você percorreu?'))
n2 = n1*0.50
n3 = n1*0.45
if n1 <= 200:
    print('O valor total da sua passagem é R$ {},'.format(n2))
else:
    print('O valor total da sua passagem é R$ {}'.format(n3))
