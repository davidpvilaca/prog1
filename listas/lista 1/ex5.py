# EXERCÍCIO - LABORATÓRIO - 05
#
# DAVID PANTALEÃO VILAÇA | TADEU DA PENHA MORAES JUNIOR
# Escreva um programa que leia um peso na Terra e o numero de um planeta e imprima o valor do seu
# peso neste planeta. A relacão de planetas e dada a seguir, juntamente com o valor das gravidades
# relativas  Terra:
# Numero Gravidade Relativa Planeta
#        | 1 | 0.37 Mercurio|
#        | 2 | 0.88 Vênus   |
#        | 3 | 0.38 Marte   |
#        | 4 | 2.64 Jupiter |
#        | 5 | 1.15 Saturno |
#        | 6 | 1.17 Urano   |
#        |------------------| 
          



def main():
	#mensagem para o usuario
	print("Descubra seu peso em outro planeta onde:\n |  1 = Mercurio  | 2 = Venus | 3 = Marte |\n |  4 = Jupter  | 5 = Saturno | 6 = Urano |\n") 
	
	#declaração de variavel
	op, peso,peso_p,mer,ven, marte, jup, sat, ura = 0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0;
	
	#atribuindo valor as variaveis
	op = 0; peso =0.0; peso_p = 0.0; mer = 0.37; ven = 0.88; marte = 0.38; jup = 2.64; sat = 1.15; ura = 1.17
	
	#entrada de dados\processamento
	peso = float(input("\nDigite seu peso: "))
	while peso <= 0:
		peso = float(input("\nDigite seu peso corretamente: "))
	
	op = int(input("Escolha o numero do planeta e descubra seu peso no planeta escolhido: "))

	while op <= 0 or op > 6:
		op = int(input("Escolha o numero do planeta corretamente: "))
  	
	
	#condições para o caluculo do peso 
	if op >= 1 and op <= 7:
		if op == 1:
			peso_p = peso * mer 
			print("Seu peso em Mercurio e de %.2f Kg" %(peso_p))
		if op == 2:
			peso_p = peso * ven
			print("Seu peso em Venus e de %.2f Kg" %(peso_p))
		if op == 3:
			peso_p = peso * marte
			print("Seu peso em Marte e de %.2f Kg" %(peso_p))
		if op == 4:
			peso_p = peso * jup
			print("Seu peso em Jupter e de %.2f Kg" %(peso_p))
		if op == 5:
			peso_p = peso * sat
			print("Seu peso em Saturno e de %.2f Kg" %(peso_p))
		if op == 6:
			peso_p = peso * ura
			print("Seu peso em Urano e de %.2f Kg" %(peso_p))		
	
	
if __name__ == '__main__':
	main()

