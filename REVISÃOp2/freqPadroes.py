__author__ = 'ifes'

import libplnRevisao
import sys

def criaLstPadroes(args):

    return args[2:-1]

def main():

    if len(sys.argv) > 3:

        lstPadroes = criaLstPadroes(sys.argv)

        strFile = libplnRevisao.fileToStr(sys.argv[1])

        dicPadr = libplnRevisao.freqPadroes(strFile,lstPadroes)

        lstOrdenados = libplnRevisao.ordenaDic(dicPadr)

        libplnRevisao.salvarLstTupOrdenadas(lstOrdenados,sys.argv[len(sys.argv)-1])

    else:
        print('Falta argumento para usar este programa!\n\nUsa-se: freqPadroes <arqTextNome> <padrao1> ... <padraoN> <arqSaidaNome>')

    return 0

if __name__ == '__main__':
    main()