import random

lista = ['banana', 'abacate', 'futebol', 'amor', 'facebook', 'cachorro' ]

palavra = lista[random.randint(0,len(lista)-1)]

palavra_escondida = "_ " * len(palavra)
print palavra_escondida

erros = 0
tentativas = 10

while tentativas > 0:
	
	letra_chutada = raw_input('Chute uma letra: ')
	
	tem_letra = False
	
	for pos in range(len(palavra)):
		if palavra[pos] == letra_chutada:
			tem_letra = True
			palavra_escondida = '{0}{1}{2}'.format(palavra_escondida[:pos*2], letra_chutada + " ", palavra_escondida[(pos + 1)*2:])

	if tem_letra:
		print 'Acertou!'
		print palavra_escondida
	else:
		erros = erros + 1
		tentativas = tentativas - 1
		print erros
	
print "FIM"
