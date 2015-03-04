__author__ = 'davidvilaca'
__date__ = '15.12.2014'

'''
f_buscarep ENTRA COM PARAMETRO { p (int) = o elemento que se procura } e { l (list) = a lista onde procurar }
retorna { achou (boolean) = se achou retorna True se nao achou retorna False }
'''

def f_buscarep(p,l):
  #variaveis locais
  achou = False
  i = 0
  
  #processamento
  for i in range(len(l)):
    if p == l[i]:
      achou = True
    #-
  #-
    
  return achou
#-

'''
f_uniao ENTRA COM PARAMETRO { L1 (LIST) E L2 (LIST) = AS LISTAS QUE SE QUER A UNIAO
retorna { lu (list) = A LISTA RESULTADO DA UNIAO }
'''

def f_uniao(l1,l2):
  #variaveis locais
  uni = []
  i = 0
  
  #uma lista entra toda primeiro
  uni = l1[:]
  
  #processamento
  for i in range(len(l2)):
    if not f_buscarep(l2[i],uni):
      uni.append(l2[i])
    #-
  #-
  
  return uni
#-

'''
f_intersecao ENTRA COM PARAMETRO { L1 (LIST) E L2 (LIST) = AS LISTAS QUE SE QUER A INTERSECAO
retorna { li (list) = A LISTA RESULTADO DA INTERSECAO }
'''

def f_intersecao(l1,l2):
  #variaveis locais
  i, j, li, menor = 0,0,[],0
  
  #processamento
  for i in range(len(l1)):
    for j in range(len(l2)):
      if l1[i] == l2[j]:
        if not f_buscarep(l1[i],li):
          li.append(l1[i])
        #-
      #-
    #-
  #-
  
  return li
#-

def main():
  #variaveis
  l1,l1a, l2, l2a, l3, i, lu, li = [],[],[],[],[],0,[],[]
  aux = ""
  
  #entrada de dados
  l1 = [1,4,3,2,6,5,9,1,2,5]
  l2 = [12,2,13,3,14,4,15]
  
    #eliminar elementos repetidos
  for i in range(len(l1)):
    if not f_buscarep(l1[i],l1a):
      l1a.append(l1[i])
    #-
  #-
    
  for i in range(len(l2)):
    if not f_buscarep(l2[i],l2a):
      l2a.append(l2[i])
    #-
  #-
  
  print(l1)
  print(l2,'\n\n')
  
  
  #uniao
  lu = f_uniao(l1a,l2a)
  aux = ","
  print('Uniao: {',end="")
  for i in range(len(lu)):
    if i == len(lu)-1:
      aux = ""
    print(str(lu[i])+aux,end="")
  print('}')
  
  #intersecao
  li = f_intersecao(l1a,l2a)
  aux = ","
  print('Intersecao: {',end="")
  for i in range(len(li)):
    if i == len(li)-1:
      aux = ""
    print(str(li[i])+aux,end="")
  print('}')
  
  return 0

if __name__ == '__main__':
	main()

