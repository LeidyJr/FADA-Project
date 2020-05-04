listofkeys=[1,2,3,4,5]
dic={x: x ** 2 for x in listofkeys}
print(dic)

caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}
caballeros.items()
caballeros.keys()
caballeros.values()

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
double_dict1 = {k*2:v*2 for (k,v) in dict1.items()}
print(double_dict1)

#reversing a tuple
tp=(('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5))
print(tp[::-1])#reversing external tuples
print(tp[0][::-1])#reversing intrnal tuple
#tuple to dict
print(dict(tp))

my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dv = {k: my_list[-k] for k in my_list if k<=len(my_list)/2}
print(dv)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)