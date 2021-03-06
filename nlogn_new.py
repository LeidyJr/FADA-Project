import math
from time import time
grandezaPartesMax=0
def minYmaxParticipante():
    arrayMin = []
    arrayMax = []
    minIn = 0
    maxIn = 0
    salidaMax = "El animal que participo en mas escenas dentro del espectaculo fue"
    salidaMin = "El animal que menos participo en escenas dentro del espectaculo fue"
    for i in range(1, len(arrayOcurrencias)):
        if i == 1:
            if arrayOcurrencias[i-1] < arrayOcurrencias [i]:
                maxIn = arrayOcurrencias[i]
                minIn = arrayOcurrencias[i-1]
                arrayMin.append(i-1)
                arrayMax.append(i)
            else:
                minIn = arrayOcurrencias[i]
                maxIn = arrayOcurrencias[i-1]
                arrayMin.append(i)
                arrayMax.append(i-1)
        else:
            if arrayOcurrencias[i] < minIn:
                minIn = arrayOcurrencias[i]
                arrayMin.clear()
            if arrayOcurrencias[i] > maxIn:
                maxIn = arrayOcurrencias[i]
                arrayMax.clear()
            if minIn == arrayOcurrencias[i]:
                arrayMin.append(i)
            if maxIn == arrayOcurrencias[i]:
                arrayMax.append(i)
    for i in range(len(arrayMax)):
        salidaMax = salidaMax+" "+str(grandezas[arrayMax[i]+1])+","
    salidaMax = salidaMax+" con "+str(maxIn)+" escenas"
    for i in range(len(arrayMin)):
        salidaMin = salidaMin+" "+str(grandezas[arrayMin[i]+1])+","
    salidaMin = salidaMin+" con "+str(minIn)+" escenas"
    print(salidaMax)
    print(salidaMin)

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

def organizarRepeticiones(arrayIn, pos):
    if arrayIn[pos][0] == arrayIn[pos-1][0]:
        if arrayIn[pos][2] < arrayIn[pos-1][2]:
            arrayAux = arrayIn[pos]
            arrayIn[pos] = arrayIn[pos-1]
            arrayIn[pos-1] = arrayAux
        if pos == 2:
            if arrayIn[pos-1][0] == arrayIn[pos-2][0]:
                organizarRepeticiones(arrayIn,pos-1)

def organizarEscenas(escenasIn, numEscenasIn):
    global grandezaPartesMax
    arraySalida = [[0,0] for _ in range(numEscenasIn)]
    arrayConteo = [0 for _ in range(maxEscena[0][1])]
    arrayIn = [ [math.ceil(escenasIn[i][1]-1),i, escenasIn[i][2]] for i in range(numEscenasIn)]
    
    for i in range(numEscenasIn):
        arrayConteo[arrayIn[i][0]] = arrayConteo[arrayIn[i][0]]+1
    

    for i in range(1,maxEscena[0][1]):
        arrayConteo[i] =arrayConteo[i]+ arrayConteo[i-1]
    
    
    contador = numEscenasIn-1
    for i in range(numEscenasIn):
        arraySalida[arrayConteo[arrayIn[contador][0]]-1] = arrayIn[contador]
        arrayConteo[arrayIn[contador][0]] = arrayConteo[arrayIn[contador][0]]-1
        contador -= 1
    
    for i in range(1,numEscenasIn):
        organizarRepeticiones(arraySalida,i)

    #print(arraySalida)
    grandezaTotalParte = 0
    arrayCompleto = [ [] for i in range(numEscenasIn)]
    for i in range(numEscenasIn):
        grandezaTotalParte += escenasIn[arraySalida[i][1]][1]
        arrayCompleto[i] = escenasIn[arraySalida[i][1]][0]

    #print('grandezaTotal '+ str(grandezaTotalParte))
    if grandezaPartesMax < grandezaTotalParte:
        grandezaPartesMax = grandezaTotalParte
    #print(arrayCompleto)
    return [arrayCompleto, grandezaTotalParte]

def organizarPartes(partesIn, numPartes):
    arraySalida = [[0,0] for _ in range(numPartes)]
    #rango = (n-1)*m
    arrayConteo = [0 for _ in range(grandezaPartesMax)]
    arrayIn = [ [math.ceil(partesIn[i][1]),i] for i in range(numPartes)]
    for i in range(numPartes):
        arrayConteo[arrayIn[i][0]] = arrayConteo[arrayIn[i][0]]+1
    for i in range(1,grandezaPartesMax):
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

def organizarPartesMergeSort(partesIn):
    if len(partesIn) > 1:
        mid = len(partesIn)//2
        print(mid)
        L = partesIn[:mid]
        R = partesIn[mid:]
        organizarPartesMergeSort(L)
        organizarPartesMergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i][1] < R[j][1]: 
                partesIn[k] = L[i] 
                i+=1
            else: 
                partesIn[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            partesIn[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            partesIn[k] = R[j] 
            j+=1
            k+=1

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
    organizarPartesMergeSort(partes)

    print("El orden en el que se debe presentar el espectaculo es:")

    print("apertura = "+str(aperturaOut[0][0]))
    
    for i in range(m-1):
        print("parte"+str(i+1)+" = "+str(partes[i][0]))
    
    minYmaxParticipante()

    print("La escena de menor grandeza total fue la escena "+str(minEscena[0][0]))
    print("La escena de mayor grandeza total fue la escena "+str(maxEscena[0][0]))
    
    


lista = []
apertura = []
parts = []
arrayEntrada = []
n = 0
m = 0
k = 0
x=0
y=3

archivo = open('your_file.txt', 'r')
    
with open('your_file.txt', 'r') as procfile:
    for line in procfile:
        if line.split() != []:
            lista.append(line.replace(';','').replace('{','[').replace('}',']').replace("'",'').split()[2:])

   
n = int(lista[0][0])
m = int(lista[1][0])
k = int(lista[2][0])

print(n,m,k)
animales = [lista[3][i].replace('[','').replace(',','').replace(']','') for i in range(n)]
grandezas = [int(lista[4][i].replace('[','').replace(',','').replace(']','')) for i in range(n)]

for g in range((m-1)*k):
    apertura.append([])
    for i in range(x,y):
        apertura[g].append((lista[5][i].replace('[','').replace(',','').replace(']','')))
    x +=3
    y +=3

x = 0
y = 3

for r in range(m-1):
    parts.append([])
    for t in range(k):
        parts[r].append([])
        for i in range(x,y):
            parts[r][t].append((lista[6+r][i].replace('[','').replace(',','').replace(']','')))
        x += 3
        y += 3
    x = 0
    y = 3

print(grandezas, len(grandezas))

animales = dict(zip(animales,grandezas))
grandezas = dict(zip(grandezas,animales))

print(len(grandezas.keys()))

arrayEntrada.append(apertura)

for i in range(len(parts)):
    arrayEntrada.append(parts[i])
    
maxEscena = []
minEscena = []


tiempo_inicial = time()
arrayOcurrencias = [0 for _ in range(n)]
organizarEvento(n,m,k,arrayEntrada)
tiempo_final = time()
tiempo_ejecucion = tiempo_final - tiempo_inicial
print("El tiempo de ejecución fue : ", tiempo_ejecucion)