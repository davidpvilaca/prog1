#  22/10/2014
#  Exercício prático 2
#  
#  Convertendo temperatura em Fahrenheit para Celsius
#  




def main():
  #Declarando variável
  fahrenheit = 0.0
  celsius = 0.0
  #Definindo valor das variáveis
  fahrenheit = float (input ('Digite a temperatura em Fahrenheit para conversão:'))
  
  #Conversão
  celsius = (5/9)*(fahrenheit-32)
  #Mostrando o resultado
  print ('%.1f graus Fahrenheit correspondem a %.2f graus Celsius.' %(fahrenheit,celsius) )

if __name__ == '__main__':
	main()

