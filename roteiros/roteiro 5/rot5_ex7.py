# DAVID VILAÇA
# 03/11/2014
# EXERCÍCIO 7

'''
F_REGRA ENTRA COM L (LISTA)
RETORNA LISTA2 (LISTA)
'''
def f_regra(l):
	#variaveis locais
	i = 0; lista2 = []; aux = [];
	
	#processamento
	while i <= 9: #acessando as 10 posicoes da lista para a nova receber os novos valores
		if (l[i])%2 == 0: #se o resto da divisao entre o elemento acessado e 2 for 0 eh par
			lista2.append(l[i]*5)
		elif (l[i]%2) != 0: #se o resto for diferente de 0 eh impar
			lista2.append(l[i]+5)
		i += 1 #contador/interrompe o loop
		#--fim if--
	#--fim while--
	return (lista2)
	
#--fim f_regra--

def main():
	#variaveis
	entrada = 0; teste1 = []; teste2 = []; i = 0;
	#entrada de dados
	for i in range(10): #insirindo 10 elemento com loop for
		teste1.append(int(input('Insira o %do numero inteiro: ' %(i+1))))
	#--fim for--
	
	#segunda lista
	teste2 = f_regra(teste1)
	
	#saida de dados
	print('\n\nA nova lista eh: ',teste2)
	
	return 0
#--fim main--

if __name__ == '__main__':
	main()
#--fim if--
