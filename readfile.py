import random

subparts = []
animales = []
grandeza = []
apertura = []
parts = []
grande = 0
n = int(input("cantidad de animales "))
m = int(input("cantidad de partes "))
while m > 60:
    m = int(input("cantidad de partes "))
k = int(input("cantidad de escenarios en cada parte "))
while k > n:
    k = int(input("cantidad de escenarios en cada parte "))

for i in range(n):
    animal = input("ingrese animal ")
    
    while animal in animales:
        print('ya existe el animal')
        animal = input("ingrese animal ")
    
    grande = int(input("ingrese la grandeza del animal "))
    while grande in grandeza:
        print('ya un animal tiene esa grandeza')
        grande = int(input("ingrese la grandeza del animal "))

    animales.append(animal)
    grandeza.append(grande)

for i in range((m-1)*k):
    apertura.append([])
    for j in range(3):
        select = animales[random.randrange(n)]
        while select in apertura[i]:
                select = animales[random.randrange(n)]
        apertura[i].append(select)




archivo = open('your_file.txt', 'w') 
archivo.write('n = '+str(n)+'\n')
archivo.write('m = '+str(m)+'\n') 
archivo.write('k = '+str(k)+'\n\n')
archivo.write('animales = '+str(animales)+'\n')
archivo.write('grandeza = '+str(grandeza)+'\n\n')
archivo.write('apertura = '+str(apertura)+'\n\n')
for i in range(m-1):
    for p in range(k):
        select = apertura[random.randrange(len(apertura))]
        while select in parts:
            select = apertura[random.randrange(len(apertura))]
        parts.append(select)
    archivo.write('parte = '+str(parts)+'\n')
    parts.clear() 
        
       

    
archivo.close()
