#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 10

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

def imprimeMatriz(matriz):
	
	i, j, aux = 0,0,0
	linhas = len(matriz)
	
	for i in range(linhas):
		aux = len(matriz[i])
		for j in range(aux):
			print (matriz[i][j], end=" ")
		print()

def f_calculaTransposta(matriz):
	i,j,linha,coluna = 0,0,len(matriz),len(matriz[0])
	
	transposta = f_criaMatriz(coluna,linha,0)
	
	for i in range(linha):
		for j in range(coluna):
			transposta[j][i] = matriz[i][j]
	
	return transposta
			

def main():
	
	#variaveis
	matriz = [[1,2,2],[5,5,4],[4,2,4]]
	imprimeMatriz(matriz)
	
	matrizT = f_calculaTransposta(matriz)
	print()
	imprimeMatriz(matrizT)
	
	return 0

if __name__ == '__main__':
	main()

