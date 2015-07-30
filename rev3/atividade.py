__author__ = 'ifes'

import random

_trocas = 0


def criaListaSorteada(qtd):
    lstNova = []
    i = 0
    while i < qtd:
        n = random.randint(10000,250000)
        if n not in lstNova:
            lstNova.append(n)
            i += 1
        #-
    #-

    return lstNova
#-

def bolha(lst):
    # Capturar quantidade de trocas
    global _trocas
    _trocas = 0

    trocou = True

    while trocou:
        trocou = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
                trocou = True
                _trocas += 1
            #-
        #-
    #-
    return lst
#-

def insercao(lst):
    # Capturar quantidade de trocas
    global _trocas
    _trocas = 0

    for i in range(1,len(lst)):
        k = 0
        while lst[i] > lst[k] and k < i:
            k += 1
        #-
        if k < i:
            lst.insert(k,lst.pop(i))
            _trocas += 1
    #-
    return lst
#-

def selecao(lst):
    # Capturar quantidade de trocas
    global _trocas
    _trocas = 0

    for i in range(len(lst)-1):
        indiceMenor = i
        for k in range(i,len(lst)):
            if lst[k] < lst[indiceMenor]:
                indiceMenor = k
        lst[indiceMenor],lst[i] = lst[i],lst[indiceMenor]
        _trocas += 1
        #-
    #-
    return lst
#-

def dicToFile(nomeArq, dicTrocas):
    arq = open(nomeArq,'wt')
    strWrite = ''
    for key in dicTrocas:
        strWrite += str(key)+':\n'
        for troca in dicTrocas[key]:
            if troca == dicTrocas[key][len(dicTrocas[key])-1]:
                strWrite += str(troca)
            else:
                strWrite += str(troca)+'\n'
        strWrite += '\n'
    #-
    arq.write(strWrite)
    arq.close()
    print('\nARQUIVO %s GRAVADO COM SUCESSO!'%nomeArq)
#-

def main():
    global _trocas

    dicTrocas = {'bolhaTable': [], 'inserção': [], 'seleção': []}

    tamanhos = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000, 12100, 14400, 16900, 19600, 22500, 25600,
28900, 32400, 36100, 40000, 44100, 48400, 52900, 57600, 62500, 67600, 72900, 78400, 84100, 90000]

    for linha in tamanhos:
        lstAux = criaListaSorteada(linha//5)
        lstBolha = lstAux[:]
        lstInserc = lstAux[:]
        lstSelec = lstAux[:]

        bolha(lstBolha)
        dicTrocas['bolhaTable'].append(_trocas)
        insercao(lstInserc)
        dicTrocas['inserção'].append(_trocas)
        selecao(lstBolha)
        dicTrocas['seleção'].append(_trocas)
        print('passou pelo tamanho: %d'%linha)
    # -fim for
    print(dicTrocas)
    dicToFile('qtdTrocasMetodos.csv',dicTrocas)

    return 0


if __name__ == '__main__':
    main()