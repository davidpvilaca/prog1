# David Vilaça
# Exercicio 03/11/2014
# Função de segundo grau


def main():
  #Declarando variáveis
  a = 0
  b = 0
  c = 0
  d = 0
  x1 = 0.0
  x2 = 0.0
  
  #Entrada de dados
  print ( 'Insira abaixo um valor inteiro para a, b e c respectivamente:' )
  a = int ( input('a:') )
  b = int ( input('b:') )
  c = int ( input('c:') )
  
  #Cálculo X' e X''
  d = (b**2)-4*(a*c)
  if a == 0 and b == 0:
    if c != 0:
      print ( 'Nenhum valor de X satisfaz a equação!' )
    else:
      print ( 'Qualquer valor de X satisfaz a equação!' )
    
  if a != 0:
    if d<0:
      print ('Solução no domínio dos números complexos!')
    else:
      x1 = (-b + (d**(1/2)) )/(2*a)
      x2 = (-b - (d**(1/2)) )/(2*a)
      print ( "X'=%.2f   X''=%.2f" %(x1,x2) )
  else:
    if b != 0:
      x1 = -c/b
      if x1 == int(x1):
        print ( "Equação do primeiro grau onde X = %.0f" %(x1) )
      else:
        print ( "Equação do primeiro grau onde X ~= %.2f" %(x1) )

  return 0

if __name__ == '__main__':
  main()

