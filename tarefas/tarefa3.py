# DAVID VILACA
# 30-11-14
# TAREFA 3


__author__ = 'davidvilaca'

#Entra com um numero float e a quantidade de aproximacoes inteiro
#Retorna a raiz aproximada float
def f_raiz (num1,qtdaprox):
	
	#decalracao de variaveis locais
	
	x1, x2, cont = 0.0,0.0,0.0
	n = 0;
	
	#processamento
	
	n = qtdaprox	#Qtd de aproximacoes
	
	x1 =  (num1)/2 #primeira aproximacao
	
	if n > 1:
		for cont in range(1,n):	#vai repetir n vezes a aproximacao indicada comecando com 1
			x2 = ((x1**2)+num1)/(2*x1)
			x1 = x2
		
	#--fim for--
	
	return (x1)
	
#--fim f_raiz--


def main():
	#Declaracao de variaveis
	num = 0; aprox = 0; qtdaprox = 0
	
	print('RAIZ QUADRADA APROXIMADA (NEWTON RAPHSON)\n\n')
	
	
	#Entrada de dados
	num = float ( input('Insira um numero positivo, ou <= 0 para encerrar: ') )
	
	if num <= 0:
		return 0
	#--fim if--
	
	
	#processamento
	while num > 0:
		
		qtdaprox = int ( input('Insira a quantidade de aproximacoes: ') )
		while qtdaprox <= 0:	#Entrar apenas com valores maiores que zero para realizar os calculos
			print('O minimo de aproximacao necessaria e 1. Por favor insira corretamente!')
			qtdaprox = int ( input('Insira a quantidade de aproximacoes: ') )
		#--fim while--
		
		aprox = f_raiz(num, qtdaprox) #chamada da funcao que calcula raiz
		
		#Saida de dados
		print('Num = %.5f	APROX = %.4d	Raiz Quadrada = %.10f' %(num, qtdaprox, aprox) )
		
		
		num = float ( input('\n\nInsira um numero positivo, ou <= 0 para encerrar: ') )
		
	#--fim while--
	
	
	
	return 0
#--fim main--

if __name__ == '__main__':
	main()
#--fim if--
