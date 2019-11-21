import sys
from creationFunctions import createBackEndExpress, createLinting

# Isso supondo que esta sendo executado dentro da pasta de projeto desejada.


def getArgs():
    argList = sys.argv
    if(argList[1] == '-c'):
        # Opcao de criacaos
        if(argList[2] == 'backendexpress'):
            createBackEndExpress()
        if(argList[3] == '-lint'):
            createLinting()


getArgs()
