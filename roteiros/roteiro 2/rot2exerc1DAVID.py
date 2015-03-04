# DAVID VILAÇA
# 05/11/2014
# EXERCÍCIO 1 - Emprpéstimo: Mostrar o valor máximo e o valor da prestação com a entrada do salário


def main():
	#DECLARAÇÃO DE VARIÁVEIS
	salario = 0
	prestacao = 0
	
	#ENTRADA DE DADOS
	salario = int ( input('Digite seu salário bruto para o cálculo do valor do empréstimo máximo:') )
	prestacao = int ( input('Digite o valor da prestação do empréstimo:') )
	
	#ESTRUTURA DE CONTROLE
	if salario >= (30/100)*prestacao:
		print ('O empréstimo pode ser concedido!')
	else:
		print ('O empréstimo NÃO pode ser concedido!')
	
	
	#SAÍDA DE  DADOS
	

if __name__ == '__main__':
	main()

