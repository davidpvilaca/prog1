#  22/10/2014
#  Exercício prático 6
#  
#  Recebendo dois valores e imprimindo a soma, subtração e divisão entre eles
#  




def main():
  #Declarando variável
  x = 0
  y = 0
  soma = 0.0
  subtracao = 0.0
  divisao = 0.0
  #Definindo valor das variáveis
  x = int ( input ('Insira um valor inteiro:') )
  y = int ( input ('Insira outro valor inteiro:') )
  #Calculo
  soma = x+y
  subtracao = x-y
  divisao = x/y
  #Mostrando o resultado
  print ('Soma = %.2f\nSubtração=%.2f\nDivisão=%.2f' %(soma,subtracao,divisao))
  return 0
if __name__ == '__main__':
	main()

