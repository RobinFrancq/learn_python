#Tuple types
tpl=(40, 50, 40, "xyz")
print(tpl)

#OPMERKING: indien je een tuple wilt definen met slecht 1 element zet je een komma achter het element in de tuple:
#tpl2=(40,)
#print(type(tpl2))

print(tpl[3]) #Indexing
print(tpl*3) #repetition

#Toevogen of verwijderen van elementen in tuple is niet mogelijk (want het is een tuple)

# Enkele functies
print(tpl.count(40)) #Geeft de index terug
print(tpl.index("xyz"))


# converteren van lijst nr Tuple
lst=[67, 34, "XYZ"]
print(type(lst))

tpl3=tuple(lst)
print(type(tpl3))
print(tpl3)