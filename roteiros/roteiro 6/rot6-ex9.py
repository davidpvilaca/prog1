#	DAVID VILAÇA
#	ROTEIRO 6 - EXERCICIO 09

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

def f_calculaTransposta(matriz):
	i,j,linha,coluna = 0,0,len(matriz),len(matriz[0])
	
	transposta = f_criaMatriz(coluna,linha,0)
	
	for i in range(linha):
		for j in range(coluna):
			transposta[j][i] = matriz[i][j]
	
	return transposta

def f_verificaSimetrica(matriz):
	i, j, linhas, colunas, aux = 0,0,len(matriz),len(matriz[0]),0
	if linhas != colunas:
		return False
	matrizT = f_calculaTransposta(matriz)
	for i in range(linhas):
		for j in range(colunas):
			if matrizT[i][j] == matriz[i][j]:
				aux += 1
	if aux == linhas*colunas:
		return True
	else:
		return False

def main():
	
	#variaveis
	matriz = [[1,1,4],[1,5,2],[4,2,7]]
	
	print(f_verificaSimetrica(matriz))
	
	
	return 0

if __name__ == '__main__':
	main()

