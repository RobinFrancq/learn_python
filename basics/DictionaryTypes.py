#Dictionary met key en value
dict1={1:"Robin", 2:"Bartje", 3:"Bill"}
print(dict1)

# Dict functies
print(dict1.items())
k=dict1.keys()
print(k)

for i in k:
    print(i)

v=dict1.values()
print(v)

for i in v:
    print(i) 

print(dict1[3]) #Voor een specifieke value door het geven van de key
del dict1[2] #verwijderen van een element 

print(dict1)       