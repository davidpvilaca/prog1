__author__ = 'ifes'

#USEI A FUNÇÃO LEN() PORQUE USANDO ESTA O PYTHON EXCEDE O LIMITE DE RECURSÃO
def length(pLstStr):
    aux = pLstStr[:]
    if type(pLstStr) == str:
        vazio = ''
    elif type(pLstStr) == list:
        vazio = ''
    else:
        return None
    if aux == vazio:
        return 0
    else:
        return 1+length(aux[1:])
#-

def somaElems(lstNum):

    if lstNum == []:
        return 0
    elif type(lstNum[0]) == int or type(lstNum[0]) == float:
        return lstNum[0]+somaElems(lstNum[1:])
    else:
        return None
#-

def fatorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n*fatorial(n-1)
#-

def produto(x,y):
    if x == 0:
        return 0
    elif x > 0:
        return y+produto(x-1,y)
    else:
        return -produto(-x,y)
#-

def divisao(x,y):
    #Pegando sinal da divisao (sinais iguais aux positivo e sinais diferentes aux negativo)
    if (x < 0 and y > 0) or (y < 0 and x > 0):
        aux = -1
    else:
        aux = 1
    x,y = abs(x),abs(y)
    if y == 0:
        return None
    elif x == 0:
        return 0
    else:
        return (1+divisao(x-y,y))*aux

#-

def pesquisa(elem,lst):
    if lst == []:
        return False
    if lst[0] == elem:
        return True
    return pesquisa(elem,lst[1:])
#-

def raizq(n,t, r=0):
    if r == 0:
        r = n/2.5
    if abs(n-(r*r)) <= t:
        return r
    else:
        return raizq(n,t,r=((n/r)+r)/2.0)
#-

def inverte(pstr):
    if len(pstr) < 2:
        return pstr
    return pstr[len(pstr)-1]+inverte(pstr[1:len(pstr)-1])+pstr[0]
#-

##################################################
#      FUNÇÕES AUXILIARES PARA O PALÍNDROMO      #
##################################################
def achaSeps(pstr,_seps=''):

    if pstr == '':
        return _seps
    elif not pstr[0].isalnum():
        _seps += pstr[0]
    return achaSeps(pstr[1:],_seps=_seps)
#-

def removeSeps(pstr,novaStr=''):
    _seps = achaSeps(pstr)
    if pstr == '':
        return novaStr
    elif pstr[0] in _seps:
        return removeSeps(pstr[1:],novaStr)
    else:
        novaStr += pstr[0]
        return removeSeps(pstr[1:],novaStr)
#-
############## FIM AUXILIARES ####################

def isPalindromo(pstr):
    pstr = removeSeps(pstr)
    if len(pstr) < 2:
        return True
    elif pstr[0].lower() != pstr[-1].lower():
        return False
    return isPalindromo(pstr[1:-1])
#-

def maiorValor(lst):
    aux = lst[:]
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    elif lst[0] > lst[1]:
        del(aux[1])
        return maiorValor(aux)
    else:
        del(aux[0])
        return maiorValor(aux)
#-
def menorValor(lst):
    aux = lst[:]
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    if lst[0] < lst[1]:
        del(aux[1])
        return menorValor(aux)
    else:
        del(aux[0])
        return menorValor(aux)
#-

#RETORNANDO INTEIRO
def decToBin(n):
    if n == 1:
        return str(n%2)
    return int(str(decToBin(n//2))+str(n%2))
#-


def isNatural(n,c=True):
    #C é a condição que inclui o 0 ou não como número natural
    if c != True and c != False:
        return None
    elif c:
        incluir = 0
    else:
        incluir = 1
    #Fim da condição do zero
    if n == incluir:
        return True
    elif n < incluir:
        return False
    return isNatural(n-1,c)
#-

# Parâmetros iniciados com "_" é para uso somente dentro da própria rotina
def permutacoes(n,_perms=[],_cont=0):
    #Cont é só pra zerar a lista por ser mutável. Zerar a lista quando a função é execultada pela primeira vez.
    if _cont == 0:
        _perms = []
    if len(n) == 0:
        return None
    if len(n) == 1:
        return [(n[0])]
    if len(_perms) == fatorial(len(n)):
        return _perms
    else:
        aux = ()
        for i in n:
            aux += (i,)
        if _cont%2 != 0:
            n = [n[0]]+[n[-1]]+n[1:-1]
        else:
            n = [n[-1]]+n[1:-1]+[n[0]]
        _perms.append(aux)

        return permutacoes(n,_perms=_perms,_cont=_cont+1)
#-

#Permutação do PROF
def permProf(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        aux = lst[0]
        lstaux = lst[1:]
        lstresult = []

        for i in permProf(lstaux):
            for k in range(len(i)+1):
                lstresult += [i[0:k]+aux+i[k:]]
    return lstresult
#-

def main():

    l = [2,5,1,2]
    print('Soma dos elementos de %s : '%str(l)+str(somaElems(l)))
    print('Produto de 9 por -9: '+str(produto(9,-9)))
    print('Divisao de 4 por -2: '+str(divisao(4,-2)))
    print('2 está em %s ? '%str(l)+str(pesquisa(2, l)))
    print('Raiz de 3 com tolerância de 0.000005: '+str(raizq(3,0.000005)))
    print('Inversao de "Aula de recursividade": '+str(inverte('Aula de recursividade')))
    print('"Aceno boneca" é palíndromo? '+str(isPalindromo('Aceno boneca')))
    print('"Socorram-me, subi no onibus em marrocos" é palíndromo? '+str(isPalindromo('Socorram-me, subi no onibus em marrocos')))
    print('Maior valor de %s é: '%str(l)+str(maiorValor(l)))
    print('Menor valor de %s é: '%str(l)+str(menorValor(l)))
    print('21 decimal para binario: '+str(decToBin(21)))
    print('5.2 é natural? '+str(isNatural(5.2)))
    print('Permutações de "a","b","c": '+ str(permutacoes(['a','b','c'])))

    return 0
#-

if __name__ == '__main__':
    main()
#-