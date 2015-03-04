#  gerar cadeia de caracters de tamanho m >= 1
#  onde tem "1" = "10" onde tem "0" = "1"

def f_substitui01(cadeia):
	
	cadeiaaux = ""
	
	for i in range(len(cadeia)):
		if cadeia[i] == "1":
			cadeiaaux += "10"
		else:
			cadeiaaux += "1"
			
	return cadeiaaux

def f_geraCadeia(m):
	cadeia = ""
	
	cadeia = "1"
	
	while len(cadeia) <= m:
		print(cadeia)
		cadeia = f_substitui01(cadeia)
	#-
	
#-


def main():
	
	#variaveis
	m = 0
	
	m = int(input("Informe o tamanho maximo da cadeia:"))
	
	f_geraCadeia(m)
	
	return 0

if __name__ == '__main__':
	main()

