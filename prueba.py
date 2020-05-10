import math


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

    if len(maxEscena) == 0:
        maxEscena.append([escenaIn, grandezaEscena])
    else:
        if maxEscena[0][1] < grandezaEscena:
            maxEscena.clear()
            maxEscena.append([escenaIn, grandezaEscena])
    
    if len(minEscena) == 0:
        minEscena.append([escenaIn, grandezaEscena])
    else:
        if minEscena[0][1] > grandezaEscena:
            minEscena.clear()
            minEscena.append([escenaIn, grandezaEscena])
    return [escenaIn, grandezaEscena, maxIn, minIn]

def organizarEscenas(escenasIn, numEscenasIn):
    arraySalida = [[0,0] for _ in range(numEscenasIn)]
    arrayConteo = [0 for _ in range(n)]
    arrayIn = [ [math.ceil(escenasIn[i][1]/3),i, escenasIn[i][2]] for i in range(numEscenasIn)]
    #print(arrayIn)
    
    for i in range(numEscenasIn):
        arrayConteo[arrayIn[i][0]] = arrayConteo[arrayIn[i][0]]+1
        
    #print(arrayConteo)

    for i in range(1,n):
        arrayConteo[i] =arrayConteo[i]+ arrayConteo[i-1]
    
    #print(arrayConteo)

    #print('contador')
    
    contador = numEscenasIn-1
    for i in range(numEscenasIn):
        arraySalida[arrayConteo[arrayIn[contador][0]]-1] = arrayIn[contador]
        arrayConteo[arrayIn[contador][0]] = arrayConteo[arrayIn[contador][0]]-1
        contador -= 1

    #print(arraySalida)
    
    for i in range(1,numEscenasIn):
        if arraySalida[i][0] == arraySalida[i-1][0]:
            if arraySalida[i][2] < arraySalida[i-1][2]:
                arrayAux = arraySalida[i]
                arraySalida[i] = arraySalida[i-1]
                arraySalida[i-1] = arrayAux
    #print(arraySalida)

    grandezaTotalParte = 0
    arrayCompleto = [ [] for i in range(numEscenasIn)]
    for i in range(numEscenasIn):
        grandezaTotalParte += escenasIn[arraySalida[i][1]][1]
        arrayCompleto[i] = escenasIn[arraySalida[i][1]][0]

    #print('grandezaTotal '+ str(grandezaTotalParte))

    #print(arrayCompleto)
    return [arrayCompleto, grandezaTotalParte]

def organizarPartes(partesIn, numPartes):
    arraySalida = [[0,0] for _ in range(numPartes)]
    rango = (n-1)*m
    arrayConteo = [0 for _ in range(rango)]
    arrayIn = [ [math.ceil(partesIn[i][1]/numPartes),i] for i in range(numPartes)]
    for i in range(numPartes):
        arrayConteo[arrayIn[i][0]] = arrayConteo[arrayIn[i][0]]+1

    
    for i in range(1,rango):
        arrayConteo[i] =arrayConteo[i]+ arrayConteo[i-1]

    contador = numPartes-1
    for i in range(numPartes):
        arraySalida[arrayConteo[arrayIn[contador][0]]-1] = arrayIn[contador]
        arrayConteo[arrayIn[contador][0]] = arrayConteo[arrayIn[contador][0]]-1
        contador -= 1
    arrayCompleto = [ [] for i in range(numPartes)]

    for i in range(numPartes):
        arrayCompleto[i] = partesIn[arraySalida[i][1]][0]

    return arrayCompleto

def organizarEvento(n, m, k, arrayPartes):
    aperturaOut = []
    partes = []
    for i in range(m):
        escenasOrganizadas =[]
        if i == 0:
            for j in range(len(arrayPartes[i])):
                escenasOrganizadas.append(organizarEscena(arrayPartes[i][j], n))
            numEscenasApertura = (m-1)*k
            aperturaOut.append(organizarEscenas(escenasOrganizadas, numEscenasApertura))
            escenasOrganizadas.clear()
        else:
            for j in range(len(arrayPartes[i])):
                escenasOrganizadas.append(organizarEscena(arrayPartes[i][j], n))
            partes.append(organizarEscenas(escenasOrganizadas, k))
            escenasOrganizadas.clear()
        
    
    partesOut = organizarPartes(partes, m-1)

    print(aperturaOut)

    #print(aperturaOut)
    for i in range(m-1):
        print(partesOut[i])
    #print('TAMAÑO ARRAY APERTURS : ', str(len(arrayPartes)))


#------------------------------------DATOS PA CAMBIAR Y PROBAR------------------------------------------------------------
n = 9
m = 4
k = 3

animales = {'leon':9, 'panteranegra':7, 'cebra':6, 'cocodrilo':5, 'boa':4, 'loro':2, 'caiman':3, 'tigre':8, 'capibara':1}
grandezas = {9:'leon', 7:'panteranegra', 6:'cebra', 5:'cocodrilo', 4:'boa', 2:'loro', 3:'caiman', 8:'tigre', 1:'capibara'}

apertura = [['caiman', 'capibara', 'loro'], ['cocodrilo', 'capibara', 'loro'], ['boa', 'caiman', 'capibara'],['panteranegra', 'cocodrilo', 'loro'], ['tigre', 'loro', 'capibara'], ['leon', 'caiman', 'loro'], ['leon', 'cocodrilo', 'boa'], ['leon', 'panteranegra', 'cebra'], ['tigre', 'cebra', 'panteranegra']]

parte1 = [['caiman', 'capibara', 'loro'], ['tigre', 'loro', 'capibara'], ['tigre', 'cebra', 'panteranegra']]

parte2 = [['panteranegra', 'cocodrilo', 'loro'], ['leon', 'panteranegra', 'cebra'], ['cocodrilo', 'capibara', 'loro']]

parte3 = [['boa', 'caiman', 'capibara'], ['leon', 'caiman', 'loro'], ['leon', 'cocodrilo', 'boa']]

arrayEntrada = [apertura, parte3, parte1, parte2]

#------------------------------------DATOS PA CAMBIAR Y PROBAR------------------------------------------------------------

"""
n = 6
m = 3
k = 2
animales = {'Gato': 3, 'Libelula': 2, 'Ciempies': 1, 'Nutria': 6, 'Perro': 4, 'Tapir':5}
grandezas = {3: 'Gato', 2: 'Libelula', 1: 'Ciempies', 6: 'Nutria', 4: 'Perro', 5:'Tapir'}


apertura = [['Tapir', 'Nutria', 'Perro'], ['Tapir', 'Perro' ,'Gato'], ['Ciempies', 'Tapir', 'Gato'], ['Gato', 'Ciempies', 'Libelula']]
parte1 = [['Tapir', 'Nutria', 'Perro'], ['Ciempies', 'Tapir', 'Gato']]
parte2 = [['Gato', 'Ciempies', 'Libelula'], ['Tapir', 'Perro', 'Gato']]

arrayEntrada = [apertura, parte2, parte1]

------------------------------------------------------------------------------------------------------------------------------------

n = 9
m = 4
k = 3

animales = {'leon':9, 'panteranegra':7, 'cebra':6, 'cocodrilo':5, 'boa':4, 'loro':2, 'caiman':3, 'tigre':8, 'capibara':1}
grandezas = {9:'leon', 7:'panteranegra', 6:'cebra', 5:'cocodrilo', 4:'boa', 2:'loro', 3:'caiman', 8:'tigre', 1:'capibara'}

apertura = [['caiman', 'capibara', 'loro'], ['boa', 'caiman', 'capibara'], ['cocodrilo', 'capibara', 'loro'], ['panteranegra', 'cocodrilo', 'loro'], ['tigre', 'loro', 'capibara'], ['leon', 'caiman', 'loro'], ['leon', 'cocodrilo', 'boa'], ['leon', 'panteranegra', 'cebra'], ['tigre', 'cebra', 'panteranegra']]

parte1 = [['caiman', 'capibara', 'loro'], ['tigre', 'loro', 'capibara'], ['tigre', 'cebra', 'panteranegra']]

parte2 = [['panteranegra', 'cocodrilo', 'loro'], ['leon', 'panteranegra', 'cebra'], ['cocodrilo', 'capibara', 'loro']]

parte3 = [['boa', 'caiman', 'capibara'], ['leon', 'caiman', 'loro'], ['leon', 'cocodrilo', 'boa']]

arrayEntrada = [apertura, parte3, parte1, parte2]

"""


maxEscena = []
minEscena = []

arrayOcurrencias = [0 for _ in range(n)]

organizarEvento(n,m,k,arrayEntrada)
"""escenasOrganizadas = []

for i in range(len(apertura)):
    escenasOrganizadas.append(organizarEscena(apertura[i], n))

niu, x = organizarEscenas(escenasOrganizadas, len(apertura))"""
