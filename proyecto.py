import math
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
    return [escenaIn, grandezaEscena, maxIn, minIn]

def organizarEscenas(escenasIn, numEscenasIn):
    arrayConteo = [[0,0] for _ in range(n)]
    
    for i in range(numEscenasIn):
        posicion = math.ceil(escenasIn[i][1]/3)
        if arrayConteo[posicion][0] == 0:
            arrayConteo[posicion][0] = i+1
            arrayConteo[posicion][1] = escenasIn[i][1]
        else:
            if arrayConteo[posicion][1] < escenasIn[i][1]:
                arrayConteo[posicion+1][0] = i+1
                arrayConteo[posicion+1][1] = escenasIn[i][1]
            else:
                arrayAux = arrayConteo[posicion]
                arrayConteo[posicion+1] = arrayAux
                arrayConteo[posicion][0] = i+1
                arrayConteo[posicion][1] = escenasIn[i][1]
    #print(arrayConteo)
    arraySalida = []
    grandezaTotalParte = 0
    for i in range(n):
        if arrayConteo[i][0] != 0:
            grandezaTotalParte += arrayConteo[i][1]
            arraySalida.append(escenasIn[arrayConteo[i][0]-1][0])
    #print(arraySalida)
    #print("grandeza por parte "+str(grandezaTotalParte))
    return [arraySalida, grandezaTotalParte]

def organizarPartes(partesIn, numPartes):
    arrayConteo = [[0,0] for _ in range(n)]

    for i in range(numPartes):
        posicion = math.ceil(partesIn[i][1]/n)
        if arrayConteo[posicion][0] == 0:
            arrayConteo[posicion][0] = i+1
            arrayConteo[posicion][1] = partesIn[i][1]
        else:
            if arrayConteo[posicion][1] < partesIn[i][1]:
                arrayConteo[posicion+1][0] = i+1
                arrayConteo[posicion+1][1] = partesIn[i][1]
            else:
                arrayAux = arrayConteo[posicion]
                arrayConteo[posicion+1] = arrayAux
                arrayConteo[posicion][0] = i+1
                arrayConteo[posicion][1] = partesIn[i][1]
    arraySalida = []
    for i in range(n):
        if arrayConteo[i][0] != 0:
            arraySalida.append(partesIn[arrayConteo[i][0]-1][0])
    print(arraySalida[0])
    print(arraySalida[1])

    
apertura = [['Tapir', 'Nutria', 'Perro'], ['Tapir', 'Perro' ,'Gato'], ['Ciempies', 'Tapir', 'Gato'], ['Gato', 'Ciempies', 'Libelula']]
parte1 = [['Tapir', 'Nutria', 'Perro'], ['Ciempies', 'Tapir', 'Gato']]
parte2 = [['Gato', 'Ciempies', 'Libelula'], ['Tapir', 'Perro', 'Gato']]


arrayApoyo = []
arrayConteo = [0 for _ in range(n)]

escenasOrganizadas =[]
for i in range(len(apertura)):
    escenasOrganizadas.append(organizarEscena(apertura[i], n))
salida1 = organizarEscenas(escenasOrganizadas,4)

escenasOrganizadas1=[]
for i in range(len(parte1)):
    escenasOrganizadas1.append(organizarEscena(parte1[i], n))

salida2 = organizarEscenas(escenasOrganizadas1,2)

escenasOrganizadas2 = []
for i in range(len(parte2)):
    escenasOrganizadas2.append(organizarEscena(parte2[i], n))
salida3 = organizarEscenas(escenasOrganizadas2,2)

salidaPartes = [salida2,salida3]


#print(salidaPartes)

print(salida1)
organizarPartes(salidaPartes,2)
#print(parte1)
#print(parte2)   
print(arrayOcurrencias)



