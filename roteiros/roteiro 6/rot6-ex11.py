#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 11

def f_verificaMenor(matriz):
	i,j,linhas,colunas,aux = 0,0,len(matriz),0,0
	
	for i in range(linhas):
		colunas = len(matriz[i])
		for j in range(colunas):
			if i == 0 and j == 0:
				aux = matriz[i][j]
			if matriz[i][j] < aux:
				aux = matriz[i][j]
	return aux
			

def main():
	
	#variaveis
	matriz = [[5,2,5],[4,0,3],[2,7,8]]
	
	print(f_verificaMenor(matriz))
	
	return 0

if __name__ == '__main__':
	main()

