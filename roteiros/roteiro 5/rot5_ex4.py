# DAVID VILAÇA
# 03/11/2014
# EXERCÍCIO 4

'''
RECEBE UMA LISTA
RETORNA O MAIOR VALOR (FLOAT) E O MENOR VALOR (FLOAT)
'''
def f_procuramm(lista):
	#variaveis locais
	i = 0; tam = 0; numM = 0.0; numm = 0.0; j = 0;
	
	tam = len(lista)-1 #tamanho da lista
	j = tam #tamanho da lista
	numM = lista[0] #recebe o primeiro valor da lista pra fazer uma comparacao
	numm = lista[0] #recebe o primeiro valor da lista pra fazer uma comparacao
	
	#processamento
	while tam >= 0: #loop comecando da ultima posicao da lista ate a primeira
		if lista[tam] > numM: #se o elemento acessado da lista for maior que o numM
			numM = lista[tam]
		#--fim if--
		if lista[tam] < numm: #se o elemento acessado da lista for menor que o numM
			numm = lista[tam]
		#--fim if--
		
		tam -= 1 #interrompe o while
	#--fim while--
	
	return (numM,numm) #retornando as variaveis que receberam o maior e o menor elemento da lista
#--fim f_procuramm--



def main():
	#variaveis
	listaq = [0.5,2.5,30.5,5.9,0.1,0.2,3.0,9.2,12.0,1.1]; maior = 0.0; menor = 0.0;
	#considerei uma lista ja pronta para fazer mais rapido#
	
	#entrada de dados
	maior, menor = f_procuramm(listaq)
	
	#saida de dados
	print('Maior = %.2f  Menor = %.2f' %(maior,menor))
	
	return 0
#--fim main--

if __name__ == '__main__':
	main()
#--fim if--
