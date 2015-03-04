#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 15

def f_multiplicaMatriz(m1,m2):
	mat3, linha, coluna, i,j,k, acumula = [],len(m1),len(m2[0]),0,0,0,0
	
	if len(m1[0]) != len(m2):
		print("Erro! O número de colunas da primeira matriz informada não é igual ao número de linhas da segunda!")
		return 0
	
	for i in range(linha):
		mat3.append([])
		for j in range(coluna):
			acumula = 0
			for k in range(len(m1[0])):
				acumula = acumula+m1[i][k]*m2[k][j]
			#-
			mat3[i].append(acumula)
		#-
	#-
	
	return mat3
	
	
	

def main():
	
	#variaveis
	matriz1 = [[2,5,9],[3,6,8]]
	matriz2 = [[2,7],[4,3],[5,2]]
	
	produto = f_multiplicaMatriz(matriz1, matriz2)
	
	print(produto)
	
	return 0

if __name__ == '__main__':
	main()

