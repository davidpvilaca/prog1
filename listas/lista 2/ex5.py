# DAVID VILAÇA
# 10.12.2014
# EXERCÍCIO 5

__author__ = 'David_Tadeu'


'''
F_VERIFICA ENTRA COM PARAMETRO TEXTO (STRING)
RETORNA VV E VC (INTEIRO) #VV = QUANTIDADE DE VOGAIS  VC = QUANTIDADE DE CONSOANTES
'''
def f_verifica(texto):
	#variaveis locais
	vv = 0; vc = 0; tamT = 0; i = 0; j = 0;
	vogais = ['a','e','i','o','u']
	consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','ç']
	
	tamT = len(texto) #tamanho do texto
	
	#processamento
	for i in range(tamT):
		
		if texto[i] in consoantes: #se o caracter do texto na posicao i conter na lista consoantes
			vc += 1
		if texto[i] in vogais: #se o caracter do texto na posicao i conter na lista vogais
			vv += 1
	#--fim for--
	
	return (vv,vc)


def main():
	#variaveis
	string = ''; vogais = 0; consoantes = 0;
	
	#entrada de dados
	print('VERIFICACAO DE VOGAIS E CONSOANTES\n\n')
	
	string = input('Digite uma mensagem para a verificacao: ')
	
	#verificacao
	string = string.lower()
	vogais, consoantes = f_verifica(string)
	
	#saida de dados
	print('\nSua mensagem tem %d vogais e %d consoates.\n' %(vogais,consoantes))	
	
	return 0

if __name__ == '__main__':
	main()

