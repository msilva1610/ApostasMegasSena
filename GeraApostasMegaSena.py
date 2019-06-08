import itertools
import json
import sys
import datetime

from pymongo import MongoClient
import json

volante = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]

c = []

def gera_apostas():
    '''
    Gera a lista completa de apostas da mega sena. tempo m~edio 18 segundos
    A lista completa é gerada com: 50.063.860 apostas
    '''
    inicio = datetime.datetime.now()
    print('Gerando lista completa - inicio: {}'.format(inicio))
    c = list(itertools.combinations(volante, 6))
    print('Total de apostas geradas: {}'.format(len(c)))
    fim = datetime.datetime.now()
    print('Gerando lista completa - fim: {}'.format(fim))
    print('Tempo Total: {}'.format(fim-inicio))

if __name__ == '__main__':
    gera_apostas()
    