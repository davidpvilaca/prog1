# EXERCÍCIO - LABORATÓRIO - 06
#
# DAVID PANTALEÃO VILAÇA | TADEU DA PENHA MORAES JUNIOR
#
#  Elabore um programa que leia um numero inteiro e imprima todos os numeros de 1 ate o numero
# lido, e tambem o produto de todos os numeros.
#  


#funcao main
def main():
  
  #declaracao de variaveis
  num, aux1, aux2, aux3, contp = 0,0,0,0,0
  
  #entrada de dados\processamento
  aux1, aux2, aux3, contp = 0,2,1,0
  
  num = int ( input ('Informe um numero inteiro:') )   #ENTRADA DO NUMERO 1 DO TECLADO
  
  
  
  print ('\nNumeros de 1 ate %d: '%(num), end="") #Impressao de 1 ate o numero de entrada na condicao abaixo
  
  if num > aux1:
    while aux1 != num:
      aux1 += 1
      print (str(aux1)+' ',end="")
      aux3 = aux3*aux1
  else:
    while aux2 != num:
      aux2 -= 1
      print (str(aux2)+'; ',end="")
      aux3 = aux3*aux1
  #fim if
  print ('  Produto = %d' %(aux3) )
  print("")
  
	
  return 0
#fim main
if __name__ == '__main__':
	main()
#fim if

