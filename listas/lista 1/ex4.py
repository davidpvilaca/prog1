# EXERCÍCIO - LABORATÓRIO - 04
#
# DAVID PANTALEÃO VILAÇA | TADEU DA PENHA MORAES JUNIOR
#  
#  Escreva um programa que recebe como entrada trˆes notas de um aluno e calcula e mostra a m´edia
# aritm´etica dessas notas. Al´em disso, imprima uma mensagem de “Aprovado”, caso a m´edia seja
# igual ou superior a 7,0, a mensagem “Recupera¸c˜ao”, caso a m´edia se igual ou superior a 5,0 e
# inferior a 7,0, ou a mensagem “Reprovado”, caso a m´edia seja inferior a 5,0.



def main():
	print("----------------------") # ---
	print(" Media final do Curso") # mensagem para o usuario 
	print("----------------------\n") # ---
	
	#declaração de variaveis 
	ma = 0.0; mb = 0.0; mc = 0.0; media = 0.0; 
	
	# atribuição de valor
	ma = float(input("Informe a primeira nota: ")); mb = float (input("Infome a segunda nota: ")); mc = float(input("Infome a terceira nota: ")) 
	
	#processamento
	# calculo da media 
	media = (ma + mb + mc) /3;
	
	#condições para definiar a media 
	if media >= 7:
		print("\nAprovado sua media final foi %.2f; Parabens!\n" % (media))
	
	if media >=5 and media < 7:
		print("\nRecuperacao! Sua media final foi %.2f;\n " % (media))
	
	if media < 5:
		print("\nReprovado! Sua media final foi: %.2f; E inferior a 5.0;\n" % (media)) 	 

if __name__ == '__main__':
	main()

