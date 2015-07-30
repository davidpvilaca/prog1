__author__ = 'ifes'

#ordenacao por mais de uma chave
# if (lst[linha][5] > lst[linha+1][5]) or (lst[linha][5] == lst[linha+1][5] and lst[linha][6] > lst[linha+1][6]) #so troca nessa condição

def compara(la,lb):

    return (la[5] > lb[5]) or (la[5] == lb[5] and la[6] > lb[6])
#-

def bolhaTable(lst,fnCompara):

    trocou = True

    while trocou:
        trocou = False
        for i in range(len(lst)-1):
            if fnCompara(lst[i],lst[i+1]):#lst[i][0] > lst[i+1][0]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
                trocou = True
            #-
        #-
    #-
    return lst
#-

def bdToLst(nomeArq):
    arq = open(nomeArq,'rt')

    lstBd = []

    linha = arq.readline()
    linha = linha.strip()
    cabec = linha.split('|')
    linha = arq.readline()
    while linha != '':
        linha = linha.strip()
        lstBd.append(linha.split('|'))
        linha = arq.readline()

    arq.close()
    return lstBd,cabec
#-

def printTabela(cabec,bd):

    print('\n')
    for el in cabec:
        print('%10s'%str(el),end='    ')
    print('\n')
    for li in bd:
        for elem in li:
            if elem == '':
                aux = ' '*(len(cabec[li.index(elem)])-1)
                print('%10s'%str(aux),end='    ')
            else:
                print('%10s'%str(elem),end='    ')
        print('\n')
    #-
    print('\n')
#-

def main():

    # lst,cabec = bdToLst('cepbr_endereco.csv')
    lst,cabec = bdToLst('test1.txt')
    lst = bolhaTable(lst,compara)
    printTabela(cabec,lst)

    return 0

if __name__ == '__main__':
    main()