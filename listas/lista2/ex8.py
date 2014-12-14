# DAVID VILAÇA
# 13.12.2014
# EXERCÍCIO 8

'''
F_GERAL3 ENTRA COM PARAMETRO L1 E L2 (LISTAS) ORDENADAS DE MODO CRESCENTE
RETORNA L3 (LISTA) GERADA DA UNIAO DAS LISTAS L1 E L2
'''
def f_geral3(l1,l2):
	#variaveis locais
	aux,i,j,l3 = 0,0,0,[]
	taml1, taml2 = 0,0
	
	taml1 = len(l1)
	taml2 = len(l2)
	
	#processamento
	while i < taml1 and j < taml2:
		if l1[i] <= l2[j]:
			l3.append(l1[i])
			i += 1
		else:
			l3.append(l2[j])
			j += 1
	if j < taml2:
		aux = (taml2-(taml2-taml1))-1
		for j in range(aux,taml2):
			l3.append(l2[j])
	if i < taml1:
		aux = (taml1-(taml1-taml2))-1
		for i in range(aux,taml1):
			l3.append(l1[i])
			
	
	return l3

def main():
	#variaveis
	l1, l2, l3 = [],[],[]
	
	#entrada de dados
	l1 = [1,3,5,7,13,15]
	l2 = [2,4,6,8,12]
	
	#teste f_geral3
	l3 = f_geral3(l1,l2)
	
	#saida de dados
	print(l3)
	
	return 0
#--fim main--

if __name__ == '__main__':
	main()
#--fim if--
