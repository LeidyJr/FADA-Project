n = 6 #Número de animales
m = 3 #Número de partes
k = 2 #Número de escenas por parte

animales = {'ciempies':1, 'libelula':2, 'gato':3, 'perro':4, 'tapir':5, 'nutria':6} # Animales {nombre:grandeza}

apertura = [
['tapir', 'nutria', 'perro'],
['tapir', 'perro', 'gato'], 
['ciempies', 'tapir', 'gato'], 
['gato', 'ciempies', 'libelula']
]

i = 0
for j in range(len(apertura)):
	for x in apertura[i]:
		if x in animales:
			print(animales[x])
	i += 1


