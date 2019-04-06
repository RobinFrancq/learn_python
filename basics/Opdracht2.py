countries = ["Belguim", "Germany", "France"]

countries.append("England")

del countries[2]

middleIndex = len(countries)/2

countries[middleIndex] = "Spain"

print(countries)

#Oplossing

lst=["USA","UK","India","Australia"]
print(lst)
 
lst.insert(3,"Africa")
print(lst)
 
del(lst[1])
print(lst)