# EXERCÍCIO - LABORATÓRIO - 07
#
# DAVID PANTALEÃO VILAÇA | TADEU DA PENHA MORAES JUNIOR
#
#  
# Faca um programa que calcule a media aritmetica de varios valores inteiros positivos, inseridos pelo
# usuario. O final da leitura acontecera quando for lido um valor negativo.
#  


#funcao main
def main():
  
  #Declaracao de variaveis
  nip, aux1, aux2, media = 0,0,0,0.0
  
  #Entrada / processamento
  aux1, aux2 = 0,0
  print ('DIGITE UM NUMERO INTEIRO POSITIVO OU -1 PARA ABORTAR\nA ENTRADA DE NUMEROS E CALCULAR A MEDIA ARITIMETICA\n')
  
  while nip != -1:
    nip = int ( input('Numero >= 0:') ) #entrada do teclado numero inteiro
    if nip < 0 and nip != -1:
      print('ERRO! Digite novamente!\n') #entrada do teclado numero inteiro ( erro caso insira numero negativo )
    if (nip > 0):
      aux1 = aux1+nip   #variavel aux1 soma os numeros inteiros positivos inseridos
      aux2 += 1         #variavel aux2 agindo como contador para o calculo da media
    #fim if
  #fim while
  
  if aux2 == 0:
    print ('\nNenhum numero inserido!')  #evitar divisao por 0, caso nao haja numero inserido
  else:
    media = aux1/aux2
  #fim if
  
  print('\nA media aritimetica e %.2f' %(media) )
  
     
  return 0

#fim main
if __name__ == '__main__':
	main()
#fim if

