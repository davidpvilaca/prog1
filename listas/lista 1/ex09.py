# EXERCÍCIO - LABORATÓRIO - 9
#
# DAVID PANTALEÃO VILAÇA | TADEU DA PENHA MORAES JUNIOR
# 
# Questao do somatorio


#funcao main
def main():
  
  print ('Somatorio com i=1 para equacao:  i*x*y\n')
  
  #declaracao de variaveis
  resultado, n, x, y, i = 0,0,0,0,0
  
  #entrada de dados
  resultado = 0
  i = 1 #constante
  n = int(input('Digite um valor inteiro > 0 limite para i no somatório: '))
  x = int(input('Digite um valor inteiro de "x" para equacao: '))
  y = int(input('Digite um valor inteiro de "y" para equacao: '))
  
  #processamento
  while i <= n: #enquanto o n for maior ou igual ao i execulte a formula
    resultado = resultado+(n*x*y) #formula da somatoria no enunciado
    n -= 1  #n funcionando como contador tanto para o termino do while quanto para a formula da somatoria
  #fim while
  
  print ( '\nO resultado do somatorio e = %d\n' %(resultado)) #impressao do resultado na tela
  
  return 0

#fim main
if __name__ == '__main__':
    main()
#fim if
