# DAVID VILAÇA
# 13.12.2014
# EXERCÍCIO 9

'''
F_BOLHA ENTRA COM PARAMETRO L(LISTA)
NAO RETORNA. APENAS ALTERA A LISTA DE ENTRADA, COLOCANDO EM ORDEM DECRESCENTE.
'''
def f_bolha(l):
	#variaveis locais
	tam, i, j = 0,0,0
	troca = True
	
	tam = len(l)-1
	
	#processamento
	while troca:
		troca = False
		for i in range(tam):
			if l[i] < l[i+1]:
				l[i],l[i+1] = l[i+1],l[i]
				troca = True


def main():
	#variaveis
	l1 = []
	#entrada de dados
	l1 = [1,9,5,3,7,6,1,9,10,8]
	
	
	#testar f_bolha
	f_bolha(l1)
	
	print(l1)
	
	
	
	return 0
#--fim main--

if __name__ == '__main__':
	main()
#--fim if--
