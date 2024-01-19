n = input('Olá, qual seu nome?')
n1 = float(input('Qual a largura (em metros) da sua parede?'))
n2 = float(input('Qual a altura (em metros) da sua parede?'))
n3 = n1*n2 #AREA
n4 = 2 #metros quadrados
n5 = 1 #litro
n6 = (n3*n5/n4) #regra de três simples
print('Olá, {}, você vai precisar de {} litros de tinta para pintar sua parede'.format(n, n6))

