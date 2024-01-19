nome = str(input('Qual é seu nome completo?')).strip()
print('Seu nome maiúsculo é', nome.upper())
print('Seu nome minúsculo é {}'.format(nome.lower()))
print('Seu nome completo tem {}'.format(len(nome) - nome.count(' ')))
nome_1 = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome_1[0], len(nome_1[0])))

