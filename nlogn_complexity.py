from time import time

#Métodos utilizados para ordenamiento

def  OrganizarEscenas(arr,low,high): 
    global arrayConteo
    global output
    arrayConteo = [DiccionarioZoo[arr[i]] for i in range(3)]

    if DiccionarioZoo.get(arr[low]) < DiccionarioZoo.get(arr[high]):
        mini = DiccionarioZoo.get(arr[low])
        maxi = DiccionarioZoo.get(arr[high])
        
    else:
        maxi = DiccionarioZoo.get(arr[low])
        mini= DiccionarioZoo.get(arr[high])
        arr[low],arr[high] = arr[high],arr[low]

    for j in range(low+1, high):
        if  DiccionarioZoo.get(arr[j]) >= maxi: 
            arr[j],arr[high] = arr[high],arr[j]
        else:
            if DiccionarioZoo.get(arr[j]) <= mini:
                arr[j],arr[low] = arr[low],arr[j]
    
    for i in range(len(arrayConteo)):
        output[arrayConteo[i]-1]+=1 


def GrandezaMaxEscena(tamaño,arr):
    global maxEsc
    if tamaño > maxEsc:
        maxEsc = tamaño
        maxEscArr.clear()
        maxEscArr.append(arr)

def GrandezaMinEscena(tamaño,arr):
    global minEsc
    if minEsc == 0:
        minEsc = tamaño
        minEscArr.append(arr)

    if minEsc > tamaño:
        minEsc = tamaño
        minEscArr.clear()
        minEscArr.append(arr)

def TamañoEscenas(arr):
    tamaño = 0
    global promedio
    global k

    try:
        for j in range(0,2):
            
            tamaño +=DiccionarioZoo.get(arr[j])
        GrandezaMaxEscena(tamaño,arr)
        GrandezaMinEscena(tamaño,arr)
    
    except:
    
        for p in range(len(arr)):
            for j in range(0,2):
                tamaño +=DiccionarioZoo.get(arr[p][j])
            GrandezaMaxEscena(tamaño,arr[p])
            GrandezaMinEscena(tamaño,arr[p])
            tamaño = 0
    
    return tamaño

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2  
        L = arr[:mid] 
        R = arr[mid:] 
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if TamañoEscenarios(L[i]) < TamañoEscenarios(R[j]): 
                arr[k] = L[i] 
                i+=1
            else: 
                try:
                    if TamañoEscenarios(L[i]) == TamañoEscenarios(R[j]):  
                        if L[i][2] < R[j][2]:
                            arr[k] = L[i] 
                            i+=1
                        else:
                            arr[k] = R[j] 
                            j+=1
                except:
                    break
                else:
                    arr[k] = R[j] 
                    j+=1
            k+=1
          
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

#Métodos utilizados para sacar los reportes

def PromedioApertura(arr):
    tamaño = 0
    global promedio
    for j in range(0,3):
        tamaño +=DiccionarioZoo.get(arr[j])
    promedio = promedio + tamaño

def Minimo(arr):

    mini = arr[0]
    arreglo = []
    j = 0
    for i in range(1,len(arr)):
        if mini > arr[i]:
            mini = arr[i]
            arreglo.clear()
            arreglo.append(i)
        else:
            if mini == arr[i]:
                arreglo.append(i)

    print("Los animales que menos participaron fueron: ")
    
    for i in range(len(arreglo)):
        print(str(Zoo2.get(arreglo[i]+1)))
    
    print(" en "+str(mini)+" escenarios." )

def Maximo(arr):
    maxi = arr[0]
    arreglo = []
    j = 0
    for i in range(1,len(arr)):
        if maxi < arr[i]:
            maxi = arr[i]
            arreglo.clear
            arreglo.append(i)
        else:
            if maxi == arr[i]:
                arreglo.append(i)
    print("Los animales que más participaron fueron: ")
    
    for i in range(len(arreglo)):
        print(str(Zoo2.get(arreglo[i]+1)))
    
    print(" en "+str(maxi)+" escenarios. " )


#Método principal, lee el archivo, llena las estructuras de datos y llama los métodos.

if __name__ == '__main__': 
    lista = []
    apertura = []
    parts = []
    x=0
    y=3

    maxEscArr = []
    minEscArr = []
    
    maxEsc = 0
    minEsc = 0

    promedio = 0

    archivo = open('your_file.txt', 'r')
    
    with open('your_file.txt', 'r') as procfile:
        for line in procfile:
            if line.split() != []:
                lista.append(line.replace(';','').replace('{','[').replace('}',']').replace("'",'').split()[2:])

    n = int(lista[0][0])
    m = int(lista[1][0])
    k = int(lista[2][0])

    arrayConteo = [0 for _ in range(n)]
    output = [0] * n


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

   
    DiccionarioZoo= dict(zip(animales,grandezas))
    Zoo2 = dict(zip(grandezas,animales))

    tiempo_inicial = time()#Inicio tomando tiempo

    for i in range((m-1)*k):
        OrganizarEscenas(apertura[i],0,2)

    for i in range(m-1):
        for j in range(0,k):
            OrganizarEscenas(parts[i][j],0,2)
    
    mergeSort(apertura)
  
    for i in range((m-1)*k):
            PromedioApertura(apertura[i])
    
    promedio = promedio/((m-1)*k)

    for i in range(m-1):
        mergeSort(parts[i])

    mergeSort(parts)
    print('El orden en el que se debe presentar el espectáculo es: \n')
    print('Apertura: ' + str(apertura))

    for i in range(0,m-1):
        print('Parte '+str(i+1)+ str(parts[i])+": ")
    
    Minimo(output)
    Maximo(output)

    print('La escena de mayor grandeza total fue la escena: '+ str(maxEscArr))
    print('La escena de menor grandeza total fue la escena: '+ str(minEscArr))
    print('El promedio de grandeza de todo el espectáculo fue de: '+ str(promedio))

tiempo_final = time()
tiempo_ejecucion = tiempo_final - tiempo_inicial
 
print ('El tiempo de ejecucion fue:',tiempo_ejecucion) 
