#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 07

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

def f_qtdZeros(matriz):
	#var
	i, j, linhas, colunas, qtd = 0,0,len(matriz),0, 0
	
	for i in range(linhas):
		colunas = len(matriz[i])
		for j in range(colunas):
			if matriz[i][j] == 0:
				qtd += 1
	return qtd

def main():
	
	#variaveis
	matriz = f_criaMatriz(2,2,0)
	
	qtd = f_qtdZeros(matriz)
	
	print("A quantidade de zeros na matriz informada eh: %d" %(qtd))
	
	return 0

if __name__ == '__main__':
	main()

