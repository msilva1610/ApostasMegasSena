import json
import sys
import datetime


from pymongo import MongoClient
from GeraTodasApostas import Apostas

def SalvaApostasDB(Dezenas):
    print('calculando apostas ...',format(datetime.datetime.now()))
    clsApostas = Apostas()
    ListaDeApostas = clsApostas.CalculaApostas(Dezenas)
    print('conectando no banco...',format(datetime.datetime.now()))

    serverMongo = MongoClient('localhost', 27017)
    dbApostas = serverMongo['dbapostas']
    col_apostasmegasena = dbApostas['clApostas']

    i = 0
    print('enviando apostas para o banco...',format(datetime.datetime.now()))
    for aposta in ListaDeApostas:
        i += 1
        novaaposta = {'_id': i, 'dezenas': aposta}
        id_inset = col_apostasmegasena.insert_one(novaaposta).inserted_id
        if i == 1000000:
            print('Aposta salva: {} - {}'.format(id_inset, datetime.datetime.now()))
            

if __name__ == '__main__':
    print('inicio ...',format(datetime.datetime.now()))
    SalvaApostasDB(6)