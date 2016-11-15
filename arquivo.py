def potencia(numero, indice, i):
	
	print "contador: %i" %i

	if indice == 0:
		return 1
	
	return numero * potencia(numero, indice-1, i+1)

print potencia(2, 10, 1)
