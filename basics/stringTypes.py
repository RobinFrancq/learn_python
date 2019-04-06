s="You are awesome"
print(s)

s1="""You are
the Creator
of your destiny"""
print(s1)

print(s[2]) #Indexing in strings

print(s*2) #Repetition in strings

print(len(s1)) #Lengte van string

print(s[0:5]) #Slicing van strings (index 5 wordt niet meegenomen!)
print(s[0:])
print(s[:8])
print(s[-3:-1])
print(s[0:9:2]) #Slicing with step (stappen van 2 letters)
print(s[::-1])

s2 = "   You are awesome   "

print(s2.strip()) #Weghalen van de spaties
print(s2.lstrip()) #Haalt enkel spaties weg aan de linker kant
print(s2.rstrip()) #Haalt enkel spaties weg van de rechter kant

#TIP: gebruik intelliJ om de functies op een type te zien en kunnen gebruiken

print (s.find("awe")) #Find zoekt een combinatie van letters in de string en geeft de start index van de combinatie
print (s.find("awe", 0, 1)) #Functie zoekt van index 0 tot 1 maar vind geen awe in de string
print(s.count("a")) #Count telt hoe vaak een substring voorkomt in een string
print(s.replace("awesome", "super")) #Replace verandert een oude substring door een nieuwe
print(s.upper()) #Upper geeft de string in uppercase
print(s.lower()) #Lower geeft de string in lowercase
print(s.title()) #Title geeft elk woord binnen de string een hoofdletter
