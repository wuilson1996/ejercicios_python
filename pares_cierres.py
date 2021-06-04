"""Dado un string formado por (), [] y {}, escribe un programa que indique si los pares correspondientes son correctos."""
entrada = "[()]{()}{[()()]()}"
entrada2 = "[(])"
#funcion que verifica la entrada
def is_valid(entrada):
	dic = {'[':']','{':'}','(':')'}
	valid = True
	aux = []
	#toma el primer caracter y empieza a verificar si es apertura o cierre
	for character in entrada:
		if character in '({[':
			aux.append(character)
		else:
			try:
				if dic[aux[len(aux)-1]] == character:
					aux.pop(len(aux)-1)
					
				else:
					break
			except:
				valid = False
				break

	if aux:
		valid = False

	return valid

print(is_valid(entrada2))