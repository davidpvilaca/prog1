#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 03

def f_verificaMatriz(matriz):
	i,j = 0,0
	linhas = len(matriz)
	colunas = 0
	aux = 0
	
	while i < linhas:
		colunas = len(matriz[i])
		if i == 0:
			aux = colunas
		if colunas != aux:
			return False
			
		i += 1
		
	return True
			

def main():
	
	#variaveis
	matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	
	if f_verificaMatriz(matriz):
		print("É matriz")
	else:
		print("Não é matriz")
	
	return 0

if __name__ == '__main__':
	main()

