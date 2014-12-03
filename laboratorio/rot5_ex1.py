# DAVID VILAÇA
# 03/11/2014
# EXERCÍCIO 1

__author__ = 'davidvilaca'


'''
FUNCAO RECEBE (PARAM) (TYPE)
RETORNA (VALUE) (TYPE)
'''
def f_soma(vetn):
	#variaveis locais
	soma = 0.0; aux = 0; i = 0;
	
	aux = len(vetn)
	
	for i in range(aux):
		soma = soma+vetn[i]
	
	return(soma)
	
#--fim f_soma--


def main():
	#variaveis
	lista = []; cont = 0; aux = 0.0; soma = 0.0;
	
	#entrada de dados
	for cont in range(5):
		lista.append(float(input('Digite um numero para adicionar na lista: ')))
	
	#processamento
	soma = f_soma(lista)
	
	#saida de dados
	print('\n\nA soma dos elementos da lista eh %.2f\n\n' %(soma))
	
	
	
	
	return 0
#--fim main--

if __name__ == '__main__':
	main()
#--fim if--

