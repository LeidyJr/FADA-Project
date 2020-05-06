
# Python program for implementation of MergeSort 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if TamañoEscenarios(L[i]) < TamañoEscenarios(R[j]): 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
# Code to print the list 
def  OrganizarEscenarios(arr,low,high): 

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
    

def TamañoEscenarios(arr):
    tamaño = 0;
    try:
        for j in range(0,2):
            tamaño +=DiccionarioZoo.get(arr[j])
    except:
        for k in range(len(arr)):
            for j in range(0,2):
                tamaño +=DiccionarioZoo.get(arr[k][j])
    
    return tamaño

def countSort(arr): 

    arr = [DiccionarioZoo.get(p)  for q in range(len(arr)) for p in arr[q] ]

    size = n
    output = [0] * size


    # Initialize count array
    count = [0] * len(arr)
    # Store the count of each elements in count array

    for i in range(len(arr)):
        output[arr[i]-1]+=1 
    
    print(output)
    minimun(output)
    maximun(output)

def minimun(arr):
    mini = arr[0]
    arreglo = []
    j = 0
    for i in range(1,len(arr)):
        if mini > arr[i]:
            mini = arr[i]
            arreglo.clear
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
    print(arreglo)
    print("los animales que mas participaro fueron ")
    
    for i in range(len(arreglo)):
        print(str(Zoo2.get(arreglo[i]+1)))
    
    print("en "+str(maxi)+" escenarios" )
    # driver code to test the above code 
if __name__ == '__main__': 
    n = 6
    m = 3
    k = 2

    animales = ['Gato', 'Libelula', 'Ciempies', 'Nutria', 'Perro', 'Tapir'];
    grandezas = [3, 2, 1, 6, 4, 5];

    DiccionarioZoo= {'Gato': 3, 'Libelula': 2, 'Ciempies': 1, 'Nutria': 6, 'Perro': 4, 'Tapir':5}
    
    Zoo2 = {3:'Gato',  2:'Libelula', 1:'Ciempies', 6:'Nutria', 4:'Perro', 5:'Tapir'}

    ##OrdenGA = Orden(animales,grandezas)
        
    apertura = [['Tapir', 'Nutria', 'Perro'], ['Tapir', 'Perro' ,'Gato'], ['Ciempies', 'Tapir', 'Gato'], ['Gato', 'Ciempies', 'Libelula']]

    parte1 = [['Tapir', 'Nutria', 'Perro'], ['Ciempies', 'Tapir', 'Gato']]

    parte2 = [['Gato', 'Ciempies', 'Libelula'], ['Tapir', 'Perro','Gato']]

    
    

    
    for i in range((m-1)*k):
        OrganizarEscenarios(apertura[i],0,2)
    
    for i in range(0,k):
        OrganizarEscenarios(parte1[i],0,2)
        OrganizarEscenarios(parte2[i],0,2)
    
    
    
    mergeSort(apertura)
    mergeSort(parte1)
    mergeSort(parte2)
    
    parts = [parte1]+[parte2]
    mergeSort(parts)

    print('apertura ' + str(apertura))
    for i in range(0,m-1):
        print('Parte '+str(i+1)+ str(parts[i]))
    
    apertura.extend(parte1)
    apertura.extend(parte2)
    
    print(countSort(apertura))
