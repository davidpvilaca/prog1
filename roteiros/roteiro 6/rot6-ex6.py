#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 06

def f_verificaQuadrada(matriz):
	i, j, aux  = 0,0,0
	linhas = len(matriz)
	for i in range(linhas):
		colunas = len(matriz[i])
		if linhas == colunas:
			aux += 1
		
	if aux == linhas:
		return True
	else:
		return False

def main():
	
	#variaveis
	matrizA = [[0,0,0],[0,0,0],[0,0,0]]
	
	if f_verificaQuadrada(matrizA):
		print("Eh quadrada")
	else:
		print("Não é quadrada")
	
	
	return 0

if __name__ == '__main__':
	main()

