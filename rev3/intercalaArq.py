__author__ = 'david'
import sys

def _err(errNumber):

    if errNumber == 0:
        print('''
        \tErro de parâmetro. Usa-se: python3 intercalaArq.py <arq1>,type <arq2>,type <arqN>,type *
        \t*Type opicional! Valor default: String
        \tEx: python3 intercalaArq.py texto1.txt,int texto2.txt,int texto3.txt,float
        ''')
    #-
#-

def closeArqs(lstAqrs,posArq='arq'):
    for arq in lstAqrs:
        arq[posArq].close()
    #-
#-

def sucess(event):
    print('''
    \t%s realizado(a) com sucesso!
    '''%event)
#-

def minVal(plst):
    lstAux = []
    cont = 0
    for i in range(len(plst)):
        if plst[i]  == '':
            cont += 1
        else:
            lstAux.append(plst[i])
        #-
    #-

    if len(lstAux) == 0:
        menor = ''
        indice = -1
    else:
        menor = min(lstAux)
        indice = lstAux.index(menor)
        indice += cont

    return menor,indice
#-

def intercalaArq(lstArqs):

    arqMerge = open('mergeResult.txt','wt')
    menor = 0
    indice = 0

    lstAtuais = []
    #criando lstAtuais
    for arq in lstArqs:
        lstAtuais.append(arq['tipo'](arq['arq'].readline()))
    #-

    while menor != '' and indice != -1:

        for i in range(len(lstArqs)):
            if lstArqs[i]['trocou']:
                linha = lstArqs[i]['arq'].readline()
                if linha != '':
                    lstAtuais[i] = lstArqs[i]['tipo'](linha)
                else:
                    lstAtuais[i] = linha
        #-

        menor,indice = minVal(lstAtuais)

        for arq in lstArqs:
            arq['trocou'] = False
        #-

        arqMerge.write(str(menor)+'\n')

        lstArqs[indice]['trocou'] = True
    #-
    arqMerge.close()

    return sucess('Intercalação')
#-

def main():

    if len(sys.argv) < 3:
        _err(0)
    else:
        lstArquivos = []
        for i in range(1,len(sys.argv)):
            nome = sys.argv[i]
            tipo = str
            if sys.argv[i].find(',') != -1:
                lstAux = sys.argv[i].split(',')
                nome = lstAux[0]
                if lstAux[1] == 'int':
                    tipo = int
                elif lstAux[1] == 'float':
                    tipo = float
                else:
                    tipo = str
            #-
            lstArquivos.append({'arq': open(nome,'rt'),'tipo': tipo, 'trocou': False})
        #-

        intercalaArq(lstArquivos)
        closeArqs(lstArquivos)
    #-

    return 0
#-
if __name__ == '__main__':
    main()
