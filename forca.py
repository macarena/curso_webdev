import random

lista = ['banana', 'abacate', 'futebol', 'amor', 'facebook', 'cachorro' ]

palavra = 'abacate'

print "_ " * len(palavra)

erros = 0

letra_chutada = raw_input('Chute uma letra: ')

tem_letra = False

for letra in palavra:
	if letra == letra_chutada:
		tem_letra = True

if tem_letra:
	print 'Acertou!'
else:
	erros = +1

print erros
