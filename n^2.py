def insertionSortescenarios(arr): 
    
    global arrayConteo
    global output
    global DiccionarioZoo,DiccionarioGrandezaZoo

    arrayConteo = [DiccionarioZoo[arr[i]] for i in range(3)]

    for i in range(1, len(arr)): 
  
        key = DiccionarioZoo[arr[i]]
  
        j = i-1
        while j >=0 and key < DiccionarioZoo[arr[j]] : 
                arr[j+1] = arr[j] 
                j -= 1
        
        arr[j+1] = DiccionarioGrandezaZoo[key]
    
    for i in range(len(arrayConteo)):
        output[arrayConteo[i]-1]+=1 

    
    
def insertionSortParts(arr): 

    for i in range(0, len(arr)): 
        for j in range (i+1, len(arr)):
            if TamañoEscenarios(arr[i]) > TamañoEscenarios(arr[j]):
                save = arr[i] 
                arr[i] = arr[j]
                arr[j] = save
        
        
  
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
        print(str(DiccionarioGrandezaZoo.get(arreglo[i]+1)))
    
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
        print(str(DiccionarioGrandezaZoo.get(arreglo[i]+1)))
    
    print("en "+str(maxi)+" escenarios" )
# driver code to test the above code 
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
    DiccionarioGrandezaZoo = dict(zip(grandezas,animales))

    for i in range((m-1)*k):
            promedioapertura(apertura[i])
    
    promedio = promedio/((m-1)*k)
    
    for i in range((m-1)*k):
        insertionSortescenarios(apertura[i])
    
    insertionSortParts(apertura)
   
    for i in range(m-1):
        for j in range(0,k):
            insertionSortescenarios(parts[i][j])

    for i in range(m-1):
        insertionSortParts(parts[i])
    
    
    insertionSortParts(parts)

    print('apertura ' + str(apertura))

    for i in range(0,m-1):
        print('Parte '+str(i+1)+ str(parts[i]))
    
    minimun(output)
    maximun(output)

    print('La escena de mayor grandeza total fue la escena '+ str(maxEscArr))
    print('La escena de menor grandeza total fue la escena '+ str(minEscArr))
    print('El promedio de grandeza de todo el espect ́aculo fue de'+ str(promedio))

