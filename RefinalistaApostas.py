import json
import sys
import datetime

from GeraTodasApostas import Apostas

def SomaDezenas(dezenas):
    soma = 0
    for d in dezenas:
        soma += d
    return soma


def CalculaParImpar(dezenas):
    impares = 0
    pares = 0
    SomaDezenas = 0
    for d in dezenas:
        if d % 2 != 0:
            impares += 1
        else:
            pares += 1
        SomaDezenas += d
    return impares, pares, SomaDezenas     

def ValidaApostas(ListaDeApostas):
    '''
    Valida Aposta: 
        Impares e Pares Duração: 0:02:53.174411
        Com soma Dezenas: 0:03:21.039748
    '''
    tot = 0
    idAposta = 0
    ListaRefinada = {}
    ListaRefinada['apostas'] = []
    for aposta in ListaDeApostas:
        idAposta += 1
        tot += 1
        # 01 e 02 Calcula Dezenas Impares e Pares
        impares, pares, somadasdezenas = CalculaParImpar(aposta)
        # 03 Soma das Dezenas
        # somadasdezenas = SomaDezenas(aposta)
        ListaRefinada['apostas'].append({
            'id': idAposta, 'aposta': aposta, 'impares': impares, 'pares':pares, 'SomaDasDezenas':somadasdezenas
            })
        if tot == 1000000:
            print(idAposta)
            tot = 0
    return ListaRefinada
            

            

if __name__ == '__main__':
    dezenas = 6
    inicio = datetime.datetime.now()
    print('inicio ...{}'.format(inicio))
    print('calculando apostas ...{}'.format(datetime.datetime.now()))
    clsApostas = Apostas()
    ListaDeApostas = clsApostas.CalculaApostas(dezenas)

    ListaApostasValidada = ValidaApostas(ListaDeApostas)
    # print(ListaApostasValidada)
    fim = datetime.datetime.now()
    print('fim ...{}'.format(fim))
    print('duracao ...{}'.format(fim-inicio))
    print(ListaApostasValidada['apostas'][0])
    