# DAVID VILAÇA
# 03/11/2014
# EXERCÍCIO 3

__author__ = 'davidvilaca'

'''
F_PRODUTO RECEBE A (LISTA) E X (FLOAT)
NAO RETORNA NADA POIS LISTA SAO MUTAVEIS
'''
def f_produto(a,x):
	#variaveis locais
	tam = 0; i = 0; prod = 0.0;
	
	tam = len(a)	#tam recebe o tamanho do vetor a
	
	#processamento
	for i in range(tam): #while i >= 0: .......... i -= 1 } com i recebendo len(a)-1 antes do while
		prod=float(a[i]*x)
		a[i] = prod


def main():
	
	#variaveis
	a = [] ; x = 0.0; an = []; cont = ""; aux= 0.0;
	
	#entrada de dados
	cont = input('Digite um numero para lista ou "fim" para encerrar: ')
	while cont != "fim":
		aux = float(cont)
		a.append(aux)
		cont = input('Digite um numero para lista ou "fim" para encerrar: ')
	
	x = float(input('Digite um numero para a multiplicacao da lista: '))
	
	#produto
	an = f_produto(a,x)
	
	#saida de dados
	print('\n\nLISTA MULTIPLICADA: ')
	print(a)
	
	return 0
#--fim main--

if __name__ == '__main__':
	main()
#--fim if--
