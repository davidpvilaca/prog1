# EXERCÍCIO - LABORATÓRIO - 9
#
# DAVID PANTALEÃO VILAÇA | TADEU DA PENHA MORAES JUNIOR
# 
# Escreva um programa que leia um valor e informe seus divisores em caso de nao ser primo, ou
# mostre na tela "EH PRIMO" caso contrario.


#funcao main
def main():
  
  print ('DESCUBRA OS DIVISORES DE UM NUMERO:\n')
  
  #declaracao de variaveis
  num, aux = 0,0
  
  #entrada de dados
  aux = 1 #aux inicia com 1
  num = int(input('Digite um numero: ')) #ler o numero do teclado
  
  print ('Os divisorres sao: ')
  
  #processamento
  while aux <= num: #enquanto a aux for menor ou igual ao numero digitado
    if (num%aux) == 0:  #se o resto da divisao do numero pela aux for 0
      print (' ',aux) #imprima na tela o aux que sera o divisor
      aux += 1  #condicao de parada do while
    elif (num%aux) != 0:  #se nao for divisivel
      aux += 1
  #fim while
  
  #NO ENUNCIADO PODE-SE PARA INFORMAR OS DIVISORES OU MOSTRAR "EH PRIMO" EU OPTEI POR MOSTRAR OS DIVISORES
  
  return 0

#fim main
if __name__ == '__main__':
    main()
#fim if
