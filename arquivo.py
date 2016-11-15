def potencia(numero, indice):
	
	if indice == 0:
		return 1
	
	print "Ainda não chegou a zero!!"
	print
	print

	return numero * potencia(numero, indice-1)

print potencia(2, 10)
