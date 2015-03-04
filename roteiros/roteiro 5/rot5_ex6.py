# DAVID VILAÇA
# 03/11/2014
# EXERCÍCIO 6

'''
F_TROCA ENTRA COM PLIST(LISTA)
NAO RETORNA NADA PORQUE LISTAS SAO IMUTAVEIS
'''
def f_troca(plist):
	#variaveis locais
	i = 0;
	#processamento
	for i in range(4):
		plist[i],plist[i+4] = plist[i+4], plist[i] #valores trocados na propria lista sem usar auxiliar
	
#--fim f_troca--

def main():
	#variaveis
	lista = []; tam = 0; aux = 0;
	#entrada de dados
	while tam <= 7:	#entrada de valores na lista (da pos 0 ate a pos 7)=8 posicoes
		lista.append(input('Insira a %da posicao: ' %(tam+1)))	#entrando apenas str na lista
		tam += 1 #interrompe o loop (contador)
	#--fim while--
	
	#troca das posicoes
	f_troca(lista)
	
	#impressao
	print('A nova lista eh:\n',lista)
	
	return 0
#--fim main--

if __name__ == '__main__':
	main()
#--fim if--
