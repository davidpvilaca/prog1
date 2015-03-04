#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 2

def f_imprimeMatriz(matriz):
	
	i, j, aux = 0,0,0
	linhas = len(matriz)
	
	for i in range(linhas):
		aux = len(matriz[i])
		for j in range(aux):
			print (matriz[i][j], end=" ")
		print()
		

def main():
	
	#variaveis
	matriz = [[1,0,1,1],[0,1,0,1],[1,1,1,0],[1,1,1,1]]	
	
	f_imprimeMatriz(matriz)
	
	return 0

if __name__ == '__main__':
	main()

