#animales = {'gato', 'libelula', 'ciempies', 'nutria', 'perro', 'tapir'}
#grandezas = {3, 2, 1, 6, 4, 5}

def organizarEscena(escenaIn, n):
    arrayConteo = [0 for _ in range(n)]
    for i in range(3):
        arrayConteo[animales[escenaIn[i]]-1] = arrayConteo[animales[escenaIn[i]]-1]+1
    contador = 0
    for i in range(n):
        if arrayConteo[i] == 1:        
            escenaIn[contador] = grandezas[i+1]
            contador +=1

proba = (1,2)
n = 6
m = 3
k = 2
animales = {'Gato': 3, 'Libelula': 2, 'Ciempies': 1, 'Nutria': 6, 'Perro': 4, 'Tapir':5}
grandezas = {3: 'Gato', 2: 'Libelula', 1: 'Ciempies', 6: 'Nutria', 4: 'Perro', 5:'Tapir'}
arrayU = [1,1,1]
print(arrayU.count(1))
print(animales.keys())
print(grandezas.keys())
    
apertura = [['Tapir', 'Nutria', 'Perro'], ['Tapir', 'Perro' ,'Gato'], ['Ciempies', 'Tapir', 'Gato'], ['Gato', 'Ciempies', 'Libelula']]
parte1 = [['Tapir', 'Nutria', 'Perro'], ['Ciempies', 'Tapir', 'Gato']]
parte2 = [['Gato', 'Ciempies', 'Libelula'], ['Tapir', 'Perro', 'Gato']]

#escenasIn = ['Tapir', 'Nutria', 'Perro']
#print(escenasIn)
#organizarEscena(escenasIn, n)

#print(escenasIn)

for i in range(len(apertura)):
    organizarEscena(apertura[i], n)

for i in range(len(parte1)):
    organizarEscena(parte1[i], n)

for i in range(len(parte2)):
    organizarEscena(parte2[i], n)

print(apertura)
print(parte1)
print(parte2)



