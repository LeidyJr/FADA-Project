
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
            if L[i] < R[j]: 
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
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 


def Change(parts):

    aperturagrandeza = [[Zoo.get(p)  for p in apertura[q]] for q in range(len(parts))]
    
    for x in range(len(aperturagrandeza)):
        mergeSort(aperturagrandeza[x]);
    print(aperturagrandeza);



# driver code to test the above code 
if __name__ == '__main__': 
    n = 6
    m = 3
    k = 2
    Zoo = {'Gato': 3, 'Libelula': 2, 'Ciempies': 1, 'Nutria': 6, 'Perro': 4, 'Tapir':5}
    
    apertura = [['Tapir', 'Nutria', 'Perro'], ['Tapir', 'Perro' ,'Gato'], ['Ciempies', 'Tapir', 'Gato'], ['Gato', 'Ciempies', 'Libelula']]

    parte1 = [['Tapir', 'Nutria', 'Perro'], ['Ciempies', 'Tapir', 'Gato']]

    parte2 = [['Gato', 'Ciempies', 'Libelula'], ['Tapir', 'Perro' 'Gato']]

    Change(apertura);
    
    #arr = [12, 11, 13, 5, 6, 7]  
    #print ("Given array is", end="\n")  
    #printList(arr) 
    #mergeSort(arr) 
    #print("Sorted array is: ", end="\n") 
    #printList(apertura) 
  
# This code is contributed by Mayank Khanna 
