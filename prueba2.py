def insertionSort(arr): 

    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  


def Valores(parts):

    aperturagrandeza = [[animales.get(p)  for p in apertura[q]] for q in range(len(parts))]
    sumasgrandeza = [ sum(q) for q in aperturagrandeza]
    diccionario = (dict(zip(sumasgrandeza, aperturagrandeza)))

    siguie = sorted(diccionario.items())

    for x in range(len(sumasgrandeza)):
        insertionSort(sumasgrandeza)
    print(sumasgrandeza)

    for x in range(len(aperturagrandeza)):
        insertionSort(aperturagrandeza[x]);
    print(aperturagrandeza);

    for x in range(len(aperturagrandeza)):
        insertionSort(siguie[x][1])

    newlist = [siguie[p][1] for p in range(len(siguie))]

    print(newlist)


# driver code to test the above code 
if __name__ == '__main__': 
    n = 6
    m = 3
    k = 2
    animales = {'Gato': 3, 'Libelula': 2, 'Ciempies': 1, 'Nutria': 6, 'Perro': 4, 'Tapir':5}
    
    apertura = [['Tapir', 'Nutria', 'Perro'], ['Tapir', 'Perro' ,'Gato'], ['Ciempies', 'Tapir', 'Gato'], ['Gato', 'Ciempies', 'Libelula']]

    parte1 = [['Tapir', 'Nutria', 'Perro'], ['Ciempies', 'Tapir', 'Gato']]

    parte2 = [['Gato', 'Ciempies', 'Libelula'], ['Tapir', 'Perro' 'Gato']]

    Valores(apertura);
    



# #Paso 1: Obtener un arreglo con los respectivos valores
# arr=[[],[],[],[]]#necesita generarse automáticamente (m-1)*k
# i=0
# for q in range(len(apertura)):
# 	for p in apertura[q]:
# 		if p in animales:
# 			arr[i].append(animales[p])
# 	i+=1
# print(arr)
# #Paso 2: Ordenar los sub arreglos internamente

# for i in arr:
# 	i.sort()# inserte algoritmo de ordenamiento

# print(arr)

# #Paso 3: Ordenar los sub arreglos 
# nume=0
# sumas=[]
# for i in arr:
# 	for m in i:
# 			nume += m
# 	print(i)    
# 	print(nume)
# 	sumas.append(nume)
# 	print(sumas)
# 	nume=0
