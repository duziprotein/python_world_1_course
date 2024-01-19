km = float(input('Velocidade do carro:'))
v = (km-80)*7
if km <= 80.0:
    print('Parabéns, você dirige muito bem!')
else:
    print('Você foi multado! A multa vai custar R$ {}.'.format(v))