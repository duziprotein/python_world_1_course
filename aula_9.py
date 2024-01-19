frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])
#apareceu ...e, pois na lista 2 (Vídeo) a terceira letra é ...e

#frase = 'Curso em Vídeo Python'
#dividido = frase.split()
#print(dividido[0])
#apareceu Curso, pois 0 é o primeiro item da lista


#frase = 'Curso em Vídeo Python'
#dividido = frase.split()
#print(dividido)
#apareceu ...['Curso', 'em', 'Vídeo', 'Python']


#frase = 'Curso em Vídeo Python'
#print(frase.split())
#apareceu...['Curso', 'em', 'Vídeo', 'Python']


#frase = 'Curso em Vídeo Python'
#print(frase.lower().find('vídeo'))
#apareceu 9, pois primeiro o lower jogou para minúsculo

#frase = 'Curso em Vídeo Python'
#print(frase.find('Curso'))
#apareceu 0

#frase = 'Curso em Vídeo Python'
#print(frase.find('Vídeo'))
#apareceu 9



#frase = 'Curso em Vídeo Python'
#print('Curso' in frase)
#mostrou ...True

#frase = 'Curso em Vídeo Python'
#print(frase.replace('Python', 'Android'))
#string é imutavel, muda apenas na instancia, agora para mudar de vez é:

#frase = 'Curso em Vídeo Python'
#frase = frase.replace('Python', 'Android')
#print(frase)
#apareceu...Curso em Vídeo Android



#frase = '   Curso em Vídeo Python   '
#print(len(frase.strip()))
#deu 21, pois o split remove espaco

#frase = '   Curso em Vídeo Python   '
#print(len(frase))
#deu 27,  pois colquei espaço no inicio e final

#frase = 'Curso em Vídeo Python'
#print(len(frase))
#deram 21 letras

#frase = 'Curso em Vídeo Python'
#print(frase.upper().count('O'))
#deu 3, pois jogou primeiro p letra maiuscula o upper

#frase = 'Curso em Vídeo Python'
#print(frase.count('o'))
#apareceu 3


#print("""Olá, professor!Enfim, estou pegando pesado no curso em python. Estou com aulas teórica e muitos exercícios. Por incrível que pareça, agora tudo faz sentido. A partir de segunda-feira vou preparar o sistema Spike MERS-CoV/DPP4 para smog e dinâmica molecular.""")

#frase = 'Curso em Vídeo Python'
#print(frase[::2])
#apareceu...Croe íe yhn

#frase = 'Curso em Vídeo Python'
#print(frase[1::2])
#apareceu...us mVdoPto

#frase = 'Curso em Vídeo Python'
#print(frase[1:15:2])
#apareceu...us mVdo

#frase = 'Curso em Vídeo Python'
#print(frase[1:15])
#apareceu...urso em Vídeo

#frase = 'Curso em Vídeo Python'
#print(frase[13:])
#apareceu...o Python

#frase = 'Curso em Vídeo Python'
#print(frase[:13])
#apareceu ...Curso em Víde

#frase = 'Curso em Vídeo Python'
#print(frase[3:13])
#apareceu... so em Víde

#frase = 'Curso em Vídeo Python'
#print(frase[3])
#fatiou e mostrou a letra s

#frase = 'Curso em Vídeo Python'
#print(frase)
