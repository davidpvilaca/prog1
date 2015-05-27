__author__ = 'David'

from operator import itemgetter

#SALVAR DICIONARIOS ORDENADAS EM UMA LISTA DE TUPLAS COM IDENTACAO NO ARQUIVO
def salvarLstTupOrdenadas(lstTup,nomeArq):
    arq = open(nomeArq,'wt')
    for tup in lstTup:
        for elem in tup:
            arq.write('%25s' %str(elem))
        arq.write('\n')
    arq.write('\n')

    arq.close()
    return 0
#-


def codifica(plstTokens):
    strCodificada = ''

    artigos = ['o', 'a', 'os', 'as', 'um', 'uns', 'uma', 'umas']
    preposicoes = ['de', 'do', 'da', 'das', 'dos', 'para', 'em', 'ao', 'à', 'às', 'ante', 'após', 'até', 'com', 'contra', 'de', 'desde', 'em', 'entre', 'para', 'perante', 'por', 'sem', 'sob', 'sobre', 'trás']
    conjuncoes = ['e', 'nem', 'mas' 'também', 'mas', 'porém', 'contudo', 'todavia', 'entretanto', 'ou', 'ora', 'já', 'quer' 'logo', 'pois', 'portanto']

    for token in plstTokens:
        if token.isalnum():

            if token.isalpha():
                #se é um artigo
                if token.lower() in artigos:
                    if token.islower():
                        strCodificada += 'a'
                    else:
                        strCodificada += 'A'
                #se é uma preposição
                elif token.lower() in preposicoes:
                    if token[0].islower():
                        strCodificada += 'p'
                    else:
                        strCodificada += 'P'
                #se é uma conjunção
                elif token.lower() in conjuncoes:
                    if token[0].islower():
                        strCodificada += 'c'
                    else:
                        strCodificada += 'C'
                #se é uma outra palavra maiuscula
                elif token[0].isupper():
                    strCodificada += 'M'
                elif token[0].islower():
                    strCodificada += 'm'
            else:
                strCodificada += 'N'
        else:
            strCodificada += token

    return strCodificada


def separaPal(pTexto):

    lstPals = []
    seps = achaSeparador(pTexto)

    try:
        pTexto += seps[0]
    except:
        return [pTexto]

    strBuffer = ''

    for elem in pTexto:
        if elem not in seps:
            strBuffer += elem
        elif strBuffer != '':
            lstPals.append(strBuffer)
            strBuffer = ''

    return lstPals
#-

def separaSentenca(pTexto):
    lstSentencas = []
    strBuffer = ''
    sepsSentencas = ['.', ',',';',':','?','!']

    pTexto = pTexto.strip()+sepsSentencas[0]

    for elem in pTexto:
        if elem not in sepsSentencas and elem not in '\n':
            strBuffer += elem
        elif strBuffer != '':
            lstSentencas.append(strBuffer)
            strBuffer = ''

    return lstSentencas
#-

def tokenizador(ptexto,pseps):
    lstTokens, lstPos = [],[]
    strBuffer = ''
    pos = 0
    ptexto = ptexto+pseps[0]

    for pos in range(len(ptexto)):
        if ptexto[pos] not in pseps:
            strBuffer += ptexto[pos]
        else:
            if strBuffer != '':
                lstTokens.append(strBuffer)
                lstPos.append(pos-len(strBuffer))
                strBuffer = ''
            if ptexto[pos] not in [' ', '\t']:
                lstTokens.append(ptexto[pos])
                lstPos.append(pos - len(ptexto[pos]))


    return lstTokens,lstPos
#-

def achaSeparador(pTexto):
    seps = []

    for elem in pTexto:
        if not elem.isalnum():
            if elem != '' and elem not in seps:
                seps.append(elem)

    return seps
#-

def freqPal(pTexto):
    dicFreq = {}

    lstPal = separaPal(pTexto)
    for pal in lstPal:
        if pal not in dicFreq:
            dicFreq[pal] = 1
        else:
            dicFreq[pal] += 1

    return dicFreq
#-


def fileToStr(arqNome,encoding='Unicode'):
    text = ''
    try:
        arq = open(arqNome,'rt',encoding=encoding)
    except:
        arq = open(arqNome,'rt')


    linha = arq.readline()
    while linha != '':
        text += linha
        linha = arq.readline()

    return text.strip()
#-

def freqPadroes(pTexto,lstPadroes):
    lstPadroes.sort(reverse=True)
    dicFreqPadroes = {}

    tokens, posTokens = tokenizador(pTexto,achaSeparador(pTexto))
    codTexto = codifica(tokens)

    for padrao in lstPadroes:

        while codTexto.find(padrao) != -1:
            temp = tokens[codTexto.find(padrao):codTexto.find(padrao)+len(padrao)]
            strPadraoTemp = ''

            for elem in temp:
                if elem.isalnum():
                    strPadraoTemp += elem+' '
                else:
                    strPadraoTemp += elem


            if strPadraoTemp not in dicFreqPadroes:
                dicFreqPadroes[strPadraoTemp] = 1
            else:
                dicFreqPadroes[strPadraoTemp] += 1
            codTexto = codTexto.replace(padrao, '*' * len(padrao), 1)


    return dicFreqPadroes

def removeStopWords(pTexto,plstStopWords):
    textSemSW = ''

    seps = achaSeparador(pTexto)
    strBuffer = ''
    for elem in pTexto:
        if elem not in seps:
            strBuffer += elem
        elif strBuffer != '':
            if strBuffer not in plstStopWords:
                textSemSW += strBuffer+elem
                strBuffer = ''
            else:
                textSemSW += ' '+elem
                strBuffer = ''

    return textSemSW
#-

def ordenaDic(dic,reverse=True):
    return sorted(dic.items(), key=itemgetter(1), reverse=reverse)

def main():

    text = fileToStr('bibliaprotvt.txt')

    strStopW = fileToStr('stopwords.txt').split(',')

    text = removeStopWords(text,strStopW)

    #dicFreq = freqPal(text)
    dicFreq = freqPadroes(text,['MpM','MM'])


    lstTupOrd = ordenaDic(dicFreq)


    salvarLstTupOrdenadas(lstTupOrd,'freq(MM,MPM)bibliaProt.txt')

    return 0
#-

if __name__ == '__main__':
    main()
