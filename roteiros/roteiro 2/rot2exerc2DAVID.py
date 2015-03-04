# DAVID VILAÇA
# 05/11/2014
# EXERCÍCIO 2 - 


def main():
	#DECLARAÇÃO DE VARIÁVEIS
	a = 0
	b = 0
	c = 0
	media = 0.0
	
	#ENTRADA DE DADOS
	a = int ( input('Digite o valor de a:') )
	b = int ( input('Digite o valor de b:') )
	c = int ( input('Digite o valor de c:') )
	#ESTRUTURA DE CONTROLE
	if a > b:
		if a > c:
			media=(5*a)+(2.5*b)+(2.5*c)/10
	else:
		if b > c:
			media=(5*b)+(2.5*c)+(2.5*a)/10
		else:
			media=(5*c)+(2.5*a)+(2.5*b)/10
	if a == b:
		if b == c:
			print ('A entrada não é válida!')
		else:
			if a > c:
				print ('A entrada não é válida!')
			
	
	#SAÍDA DE  DADOS
	print ( ' Sua media e %.2f ' %(media) )
	
	
	return 0

if __name__ == '__main__':
	main()

