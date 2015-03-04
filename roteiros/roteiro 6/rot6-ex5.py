#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 05

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
	
def f_verificaIdentidade(matriz):
	i, j, linhas, colunas, aux = 0,0,0,0,0
	linhas = len(matriz)
	
	if linhas==1:
		return False
	
	for i in range(linhas):
		colunas = len(matriz[i])
		for j in range(colunas):
			if i == j:
				if matriz[i][j] == 1:
					aux += 1
	if aux == linhas:
		return True
	else:
		return False

def main():
	
	#variaveis
	n = 3
	
	matriz = f_matrizIdentidade(n)
	
	if f_verificaIdentidade(matriz):
		print("É identidade")
	else:
		print("Não é identidade")
	
	
	return 0

if __name__ == '__main__':
	main()

