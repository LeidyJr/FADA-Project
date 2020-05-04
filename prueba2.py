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


#double_dict1 = {k:v*2 for (k,v) in animales.items()}
#print(double_dict1)
arr=[[],[],[],[]]#necesita generarse automáticamente (m-1)*k
i=0
for q in range(len(apertura)):
	for p in apertura[q]:
		if p in animales:
			arr[i].append(animales[p])
	i+=1
print(arr)

