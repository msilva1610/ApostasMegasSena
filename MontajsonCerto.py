ListaDeApostas = {}
ListaDeApostas['apostas'] = []
Aposta = [1,2,3,4,5,6]
id = 1
ListaDeApostas['apostas'].append({'id':id,'dezenas':Aposta})
id = 2
ListaDeApostas['apostas'].append({'id':id,'dezenas':Aposta})

multiplos = {}
multiplos['de'] = []

multiplos['de'].append({'3':1,'4':2})

id = 3
ListaDeApostas['apostas'].append({'id':id,'dezenas':Aposta, 'multiplos':multiplos['de']})


for i in range(4,11):
    id = i
    multiplos['de'].append({str(i):1})

# print(multiplos['de'])
print(ListaDeApostas)