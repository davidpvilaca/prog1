#  ler diversos numeros inteiros
#  imprima mdc entre os dois numeros

def f_calculaMDC(n1,n2):
	
	#variaveis
	mdc, resto, dividendo, divisor = 0,0,0,0
	
	dividendo = n1; divisor = n2; resto = dividendo%divisor
	
	while resto > 0:
		dividendo, divisor = divisor, resto
		resto = dividendo%divisor
	#-while
	mdc = divisor
	
	return mdc
	
#-f_calculaMDC


def main():
	
	#variaveis
	n1, n2, mdc = 0,0,0
	
	#leitura dos dados de entrada
	n1 = int(input("Informe o primeiro numero:"))
	n2 = int(input("Informe o segundo numero:"))
	
	while n1 > 0 and n2 > 0:
		mdc = f_calculaMDC(n1,n2)
		print("N1 = %d N2 = %d MDC = %d" %(n1,n2,mdc))
		n1 = int(input("Informe o primeiro numero:"))
		n2 = int(input("Informe o segundo numero:"))
	#-while
	
	return 0
#-main

if __name__ == '__main__':
	main()

