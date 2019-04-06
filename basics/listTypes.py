#In een lijst is het mogelijk verschillende types mee te geven 
lst=[10, 20, 'Robin', -10, 13.5]
print(lst);

#Indexing in een lijst (ZERO-BASED)
print(lst[3])
print(lst[3:5]) #slicing

print(lst*4) #repetition
print(len(lst)) #Het aantal elementen in de lijst

#Toevoegen en verwijderen van elementen in een lijst
lst.append(40) #Toevoegen
lst.remove('Robin') #verwijderen (ERROR indien element niet aanwezig is)
del(lst[1]) #verwijderen via de index
print(lst)

#Enkele list-functies
#lst.clear() #WERKT NIET 
print(max(lst))
print(min(lst))
lst.insert(3, 99)
print(lst)
lst.sort(reverse = True)
print(lst)
