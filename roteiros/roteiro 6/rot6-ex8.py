#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 08

def f_criaMatriz(m,n,e):
	#var
	criada, i, j = [],0,0
	
	#processamento
	for i in range(m):
		criada.append([])	
		for j in range(n):
			criada[i].append(e)
		#-
	#-
	return criada

def f_somaDiag(matriz):
	#var
	i, j, linhas, colunas = 0,0,len(matriz),0
	soma = 0
	
	for i in range(linhas):
		colunas = len(matriz[i])
		for j in range(colunas):
			if i == j:
				soma += matriz[i][j]
	return soma

def imprimeMatriz(matriz):
	
	i, j, aux = 0,0,0
	linhas = len(matriz)
	
	for i in range(linhas):
		aux = len(matriz[i])
		for j in range(aux):
			print (matriz[i][j], end=" ")
		print()

def main():
	
	#variaveis
	matriz = f_criaMatriz(3,3,1)
	soma = f_somaDiag(matriz)
	
	imprimeMatriz(matriz)
	
	print("A soma da diagonal principal eh: %d" %(soma))
	
	return 0

if __name__ == '__main__':
	main()

