import json
import sys
import datetime

from GeraTodasApostas import Apostas
  
def ContaPrimos(dezenas):
    NumerosPrimos = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    totPrimos = 0
    for d in dezenas:
        if d in NumerosPrimos:
            totPrimos += 1
    return totPrimos


def SomaDigitosDezenas(dezenas):
    soma_dos_digitos_das_dezenas = 0
    for d in dezenas:
        strdezena = str(d)
        for s in strdezena:
            soma_dos_digitos_das_dezenas += int(s)
    return  soma_dos_digitos_das_dezenas


def SomaDezenas(dezenas):
    soma = 0
    for d in dezenas:
        soma += d
    return soma


def CalculaParImparSomaDez(dezenas):
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
        # 01 e 02 Calcula Dezenas Impares e Pares - 04 Soma dezenas
        impares, pares, somadasdezenas = CalculaParImparSomaDez(aposta)
        # 05 Soma digitos das Dezenas
        SomaDosDigitosDaDezena = SomaDigitosDezenas(aposta)
        # 06 Total de Numeros Primos nas dezenas
        TotalDePrimos = ContaPrimos(aposta)
        ListaRefinada['apostas'].append({
            'id': idAposta, 'aposta': aposta, 'impares': impares, 'pares':pares, 'SomaDasDezenas':somadasdezenas, 'SomaDosDigitosDaDezena':SomaDosDigitosDaDezena, 'TotalDePrimos': TotalDePrimos
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
    
