n = 6 #Número de animales
m = 3 #Número de partes
k = 2 #Número de escenas por parte
# escena = conjunto de 3 animales

animales = {'ciempies':1, 'libelula':2, 'gato':3, 'perro':4, 'tapir':5, 'nutria':6} # Animales {nombre:grandeza}


#(m-1)*k
apertura = [
['tapir', 'nutria', 'perro'],
['tapir', 'perro', 'gato'], 
['ciempies', 'tapir', 'gato'], 
['gato', 'ciempies', 'libelula']
]


#Paso 1: Obtener un arreglo con los respectivos valores
arr=[[],[],[],[]]#necesita generarse automáticamente (m-1)*k
i=0
for q in range(len(apertura)):
	for p in apertura[q]:
		if p in animales:
			arr[i].append(animales[p])
	i+=1
print(arr)
#Paso 2: Ordenar los sub arreglos internamente

for i in arr:
	i.sort()# inserte algoritmo de ordenamiento

print(arr)

#Paso 3: Ordenar los sub arreglos 
nume=0
sumas=[]
for i in arr:
	for m in i:
			nume += m
	print(i)    
	print(nume)
