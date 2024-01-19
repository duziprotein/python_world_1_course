n1 = float(input('Comprimento da 1ºreta:'))
n2 = float(input('Comprimento da 2ºreta:'))
n3 = float(input('Comprimento da 3ºreta:'))
n4 = n1+n2
n5 = n1+n3
n6 = n2+n3
if n1 and n2 and n3 < n4 and n5 and n6:
    print("Forma triângulo.")
else:
    print('Não forma triângulo.')
