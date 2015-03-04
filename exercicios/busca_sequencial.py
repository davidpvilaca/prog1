#	DAVID VILACA
#	02-12-2014

#########################
#                       #
#   BUSCA SEQUENCIAL    #
#                       #
#########################

__author__ = 'davidvilaca'

'''
FUNCAO F_BUSCA ENTRA COM PROCURADO (INTEIRO) E COM VETOR (LISTA)
RETORNA ACHOU (BOOLEAN). SE ACHOU RETORNA TRUE, CASO CONTRARIO RETORNA FALSE
'''
def f_busca (procurado,vetor):
	#variaveis locais
	i, aux, lenl = 0,0,0
	achou = False
	
	#processamento
	lenl = len(vetor) #Quantidade de elementos do vetor
	
	while not achou and i < (lenl): #Enquanto achou == False
		
		if procurado == vetor[i]:	#Se o que se procura for achado, altera a achou para True (interrompe o loop)
			achou = True
		#--fim if--
			
		i += 1	#contador caso percorra todos elementos da lista e nao ache (interrompe o loop)
		
	#--fim while--
	
	
	return(achou) #retorna True se achou ou False se nao achou
#--fim f_busca--


def main():
	#variaveis
	vetor, aux, procura = [],"",""
	resultado = True
	
	#entrada de dados
	aux = input('Insira numeros inteiros para adicionar ou "fim" para encerrar: ')
	
	while aux != "fim":
		aux = int(aux)
		vetor.append(aux) #valor inserido no vetor
		aux = input('Insira numeros inteiros para adicionar ou "fim" para encerrar: ') #se entrar com "fim" interrompe o loop
	#--fim while--
	
		
	#busca sequencial
	print('\n\nPROCURAR NA LISTA CRIADA\n\n')
	
	procura = input('Digite um numero a ser procurado ou "fim" para encerrar: ')
	while procura != "fim":
		procura = int(procura)
		resultado = f_busca(procura,vetor) #Chama a funcao f_busca para fazer a busca
		
		if resultado: #se obtiver resultado, ou seja, resultado == True
			print('O elemento %d possui na lista criada!' %(procura))
		else:	#se NAO obtiver resultado, ou seja, resultado == False
			print('O elemento %d NAO possui na lista criada!' %(procura))
		#--fim if--
		
		procura = input('\n\nDigite um numero a ser procurado ou "fim" para encerrar: ') #se entrar com "fim" interrompe o loop
		
	#--fim while--
	
	return 0

if __name__ == '__main__':
	main()

