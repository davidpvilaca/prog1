#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 01

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
			


def main():
	
	#variaveis
	m, n, e = 0,0,"0"
	matriz = 0
	
	matriz = f_criaMatriz(m,n,e)
	
	return 0

if __name__ == '__main__':
	main()

