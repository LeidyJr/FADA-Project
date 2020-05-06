#animales = {'gato', 'libelula', 'ciempies', 'nutria', 'perro', 'tapir'}
#grandezas = {3, 2, 1, 6, 4, 5}
n = 6
m = 3
k = 2
animales = {'Gato': 3, 'Libelula': 2, 'Ciempies': 1, 'Nutria': 6, 'Perro': 4, 'Tapir':5}
grandezas = {3: 'Gato', 2: 'Libelula', 1: 'Ciempies', 6: 'Nutria', 4: 'Perro', 5:'Tapir'}

arrayOcurrencias = [0 for _ in range(n)]

def organizarEscena(escenaIn, n):
    arrayConteo = [animales[escenaIn[i]] for i in range(3)]
    grandezaEscena = 0
    maxIn = 0
    minIn = 0 
    medioIn = 0
    for i in range(1,3):
        if i == 1:
            if arrayConteo[i-1] < arrayConteo[i]:
                maxIn = arrayConteo[i]
                minIn = arrayConteo[i-1]
            else:
                maxIn = arrayConteo[i-1]
                minIn = arrayConteo[i]
        if maxIn > arrayConteo[i] and i != 1 and minIn < arrayConteo[i]:
            medioIn = arrayConteo[i]
        if maxIn < arrayConteo[i] and i !=1:
            medioIn = maxIn
            maxIn = arrayConteo[i]
            if medioIn < minIn:
                aux = minIn
                minIn = medioIn
                medioIn = aux
        if minIn > arrayConteo[i] and i != 1 :
            medioIn = minIn
            minIn = arrayConteo[i]
        #borrar  
    arrayConteo[0] = minIn
    arrayConteo[1] = medioIn
    arrayConteo[2] = maxIn
    for i in range(3):
        escenaIn[i] = grandezas[arrayConteo[i]]
        arrayOcurrencias[arrayConteo[i]-1] = arrayOcurrencias[arrayConteo[i]-1]+1
        grandezaEscena += arrayConteo[i]
    #return grandezaEscena, maxIn, minIn

proba = (1,2)

arrayU = [1,1,1]
print(arrayU.count(1))
print(animales.keys())
print(grandezas.keys())
    
apertura = [['Tapir', 'Nutria', 'Perro'], ['Tapir', 'Perro' ,'Gato'], ['Ciempies', 'Tapir', 'Gato'], ['Gato', 'Ciempies', 'Libelula']]
parte1 = [['Tapir', 'Nutria', 'Perro'], ['Ciempies', 'Tapir', 'Gato']]
parte2 = [['Gato', 'Ciempies', 'Libelula'], ['Tapir', 'Perro', 'Gato']]

"""escenasIn = ['Tapir', 'Nutria', 'Perro']
print(escenasIn)
organizarEscena(escenasIn, n)

print(escenasIn)"""


arrayApoyo = []
arrayConteo = [0 for _ in range(n)]

for i in range(len(apertura)):
    organizarEscena(apertura[i], n)
    #arrayConteo[grandezaIn/3]
    

for i in range(len(parte1)):
    organizarEscena(parte1[i], n)

for i in range(len(parte2)):
    organizarEscena(parte2[i], n)

print(apertura)
print(parte1)
print(parte2)   
print(arrayOcurrencias)



