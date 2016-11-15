def potencia(numero, indice):
	
	if indice == 0:
		return 1
	
	return numero * potencia(numero, indice-1)

print potencia(2, 10)
