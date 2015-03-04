# EXERCÍCIO - LABORATÓRIO - 02
#
# DAVID PANTALEÃO VILAÇA | TADEU DA PENHA MORAES JUNIOR
#
# Recebe como entrada a idade de uma pessoa, determina e imprime a sua classificação: (menor de idade, adulto ou idoso)


#FUNÇÃO MAIN
def main():
  #Declaração de variáveis
  idade = 0
  
  #Entrada de dados
  print ('----------------------')
  print ('|Classificação etária|')
  print ('----------------------\n')
  idade = int ( input('Por favor, insira sua idade para classificarmos:') )
  
  while idade < 0:
    idade = int ( input('Não existe idade negativa, por favor insira sua idade corretamente para classificarmos:') )
  
  #Processamento de dados
  if idade <= 17:
    print ( 'Você é menor de idade!' )
  else:
    if idade > 17 and idade <= 64:
      print ( 'Você é adulto!' )
    else:
      print ( 'Você é idoso!' )
  
  
  return 0

#FIM MAIN
if __name__ == '__main__':
	main()
#FIM IF

