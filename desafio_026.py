n1 = str(input('Digite uma frase')).strip() .upper()
print('A letra A aparece', n1.count('A'),'vezes.')
print('A primeira letra A da frase está na posição', n1.find('A')+1)
print('A última letra A da frase está na posição', n1.rfind('A')+1 - n1.count(' '))


