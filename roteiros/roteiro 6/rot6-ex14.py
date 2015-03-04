#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 14

def imprimeMatriz(matriz):
	
	i, j, aux = 0,0,0
	linhas = len(matriz)
	
	for i in range(linhas):
		aux = len(matriz[i])
		for j in range(aux):
			print (matriz[i][j], end=" ")
		print()

def f_somaMatriz(m1,m2):
	i, j, aux, linhas, colunas, soma = 0,0,0,len(m1),0,[]
	
	if len(m1) != len(m2):
		return 0
	if len(m1[0]) != len(m2[0]):
		return 0
	
	for i in range(linhas):
		colunas = len(m1[i])
		soma.append([])
		for j in range(colunas):
			soma[i].append(m1[i][j]+m2[i][j])
	#-
	return soma

def main():
	
	#variaveis
	matrizA = [[1,1,3],[3,4,2],[5,5,5]]
	matrizB = [[2,1,3],[1,1,6],[3,0,-9]]
	soma = []
	
	soma = f_somaMatriz(matrizA,matrizB)
	
	imprimeMatriz(matrizA)
	print()
	imprimeMatriz(matrizB)
	print()
	imprimeMatriz(soma)
	
	return 0

if __name__ == '__main__':
	main()

