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
                if TamañoEscenarios(L[i]) == TamañoEscenarios(R[j]):
                    if L[i][2] < R[i][2]:
                        arr[k] = L[i] 
                        i+=1
                    else:
                        arr[k] = L[j] 
                        j+=1
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



def  OrganizarEscenarios(arr,low,high): 
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

def TamañoEscenarios(arr):
    tamaño = 0
    global promedio
    global k
    try:
        for j in range(0,k):
            
            tamaño +=DiccionarioZoo.get(arr[j])
        GrandezaMaxEscena(tamaño,arr)
        GrandezaMinEscena(tamaño,arr)
    except:
        for p in range(len(arr)):
            for j in range(0,k):
                tamaño +=DiccionarioZoo.get(arr[p][j])
            GrandezaMaxEscena(tamaño,arr[p])
            GrandezaMinEscena(tamaño,arr[p])
    
    return tamaño

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
    

def promedioapertura(arr):
    tamaño = 0
    global promedio
    for j in range(0,3):
        tamaño +=DiccionarioZoo.get(arr[j])
    promedio = promedio + tamaño

def minimun(arr):

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

    print("los animales que menos participaro fueron ")
    
    for i in range(len(arreglo)):
        print(str(Zoo2.get(arreglo[i]+1)))
    
    print("en "+str(mini)+" escenarios" )

def maximun(arr):
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
    print("los animales que mas participaro fueron ")
    
    for i in range(len(arreglo)):
        print(str(Zoo2.get(arreglo[i]+1)))
    
    print("en "+str(maxi)+" escenarios" )

if __name__ == '__main__': 
    n = 9
    m = 4
    k = 3

    maxEscArr = []
    minEscArr = []
    
    maxEsc = 0
    minEsc = 0

    promedio = 0

    arrayConteo = [0 for _ in range(n)]
    output = [0] * n

    animales = ['leon', 'panteranegra', 'cebra', 'cocodrilo', 'boa', 'loro', 'caiman', 'tigre', 'capibara'];
    grandezas = [9, 7, 6, 5, 4, 2, 3, 8, 1];

    DiccionarioZoo= dict(zip(animales,grandezas))
    
    
    Zoo2 = dict(zip(grandezas,animales))

    apertura = [['caiman', 'capibara', 'loro'], 
                ['boa', 'caiman', 'capibara'], 
                ['cocodrilo', 'capibara', 'loro'], 
                ['panteranegra', 'cocodrilo', 'loro'], 
                ['tigre', 'loro', 'capibara'], 
                ['leon', 'caiman', 'loro'], 
                ['leon', 'cocodrilo', 'boa'], 
                ['leon', 'panteranegra', 'cebra'], 
                ['tigre', 'cebra', 'panteranegra']]

    parte1  =  [['caiman','capibara','loro'], 
                ['tigre', 'loro', 'capibara'], 
                ['tigre', 'cebra', 'panteranegra']]

    parte2  =  [['panteranegra', 'cocodrilo', 'loro'], 
                ['leon', 'panteranegra', 'cebra'], 
                ['cocodrilo', 'capibara', 'loro']]

    parte3  =  [['boa', 'caiman', 'capibara'], 
                ['leon', 'caiman', 'loro'], 
                ['leon', 'cocodrilo', 'boa']]

    
    for i in range((m-1)*k):
        OrganizarEscenarios(apertura[i],0,2)

    for i in range(0,k):
        OrganizarEscenarios(parte1[i],0,2)
        OrganizarEscenarios(parte2[i],0,2)
        OrganizarEscenarios(parte3[i],0,2)
    
    mergeSort(apertura)
  
    for i in range((m-1)*k):
            promedioapertura(apertura[i])
    
    promedio = promedio/((m-1)*k)

    mergeSort(parte1)
    mergeSort(parte2)
    mergeSort(parte3)


    parts = [parte1]+[parte2]+[parte3]
    mergeSort(parts)
    print('apertura ' + str(apertura))

    for i in range(0,m-1):
        print('Parte '+str(i+1)+ str(parts[i]))
    
    minimun(output)
    maximun(output)

    print('La escena de mayor grandeza total fue la escena '+ str(maxEscArr))
    print('La escena de menor grandeza total fue la escena '+ str(minEscArr))
    print('El promedio de grandeza de todo el espect ́aculo fue de'+ str(promedio))