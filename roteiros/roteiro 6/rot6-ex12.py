#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 12

def f_somaLinhas(mat):
	i, j, soma, linhas, colunas, aux = 0,0,[],len(mat),0,0
	
	while i < linhas:
		colunas = len(mat[i])
		for j in range(colunas):
			aux = aux+mat[i][j]
		soma.append(aux)
		aux = 0
		
		i += 1
	
	return soma

def main():
	
	#variaveis
	matriz = [[1,1,1],[2,2,2]]; soma = []
	
	soma = f_somaLinhas(matriz)
	
	print(soma)
	
	return 0

if __name__ == '__main__':
	main()

