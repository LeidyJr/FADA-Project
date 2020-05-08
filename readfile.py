lista = []
archivo = open('your_file.txt', 'r')
with open('your_file.txt', 'r') as procfile:
    for line in procfile:
        if line.replace(';','').split() != []:
            lista.append(line.replace(';','').replace('{','[').replace('}',']').replace("'",'').split()[2:])

n = int(lista[0][0])
m = int(lista[1][0])
k = int(lista[2][0])

animales = [lista[3][i].replace('[','').replace(',','').replace(']','') for i in range(n-1)]
grandeza = [lista[4][i].replace('[','').replace(',','').replace(']','') for i in range(n-1)]

apertura = [[lista[5][i].replace('[','').replace(',','').replace(']','') for i in range((m-1)*k)] for j in range(n-1)]
