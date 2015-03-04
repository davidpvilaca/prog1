#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 04

def imprimeMatriz(matriz):
	
	i, j, aux = 0,0,0
	linhas = len(matriz)
	
	for i in range(linhas):
		aux = len(matriz[i])
		for j in range(aux):
			print (matriz[i][j], end=" ")
		print()


def f_matrizIdentidade(n):
	
	i,j, matriz = 0,0,[]
	
	for i in range(n):
		matriz.append([])
		for j in range(n):
			if i == j:
				matriz[i].append(1)
			else:
				matriz[i].append(0)
	
	return matriz
			

def main():
	
	#variaveis
	n = 5
	
	
	imprimeMatriz(f_matrizIdentidade(n))
	
	return 0

if __name__ == '__main__':
	main()

