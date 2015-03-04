# DAVID VILAÇA
# 05/11/2014
# EXERCÍCIO A REPETIÇÕES


def main():
	#DECLARAÇÃO DE VARIÁVEIS
	a = 0
	b = 0
	v = 0
	v2 = 0
	
	
	#ENTRADA DE DADOS
	a = int (input('Informe um valor a:'))
	b = int (input('Informe um valor b>a:'))
	while a>b:
		print('Informe um valor maior que A!')
		b = int (input('Informe um valor b>a:'))
		
	
	#ESTRUTURA DE CONTROLE
	v=str(a)
	v2=a
	while a<=b:
		a=a+1
		if a<b:
			v=v+","+str(a)
	print ('Os números são [%s]' %(v) )
	
	while a<=b:
		
	
	return 0
	
	#SAÍDA DE  DADOS

if __name__ == '__main__':
	main()
