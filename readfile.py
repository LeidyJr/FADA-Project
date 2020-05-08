lista = []
apertura = []
parts = []
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

animales = [lista[3][i].replace('[','').replace(',','').replace(']','') for i in range(n-1)]
grandeza = [lista[4][i].replace('[','').replace(',','').replace(']','') for i in range(n-1)]

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
#parts = [[lista[6][i].replace('[','').replace(',','').replace(']','') for i in range(3)] for j in range(m-1)]
print(parts)
