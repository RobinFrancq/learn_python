# Klasse zonder encapsulatie
class Student:
    
    def __init__(self):
        # Deze fields zijn public
        self.id = 123
        self.name = "Robin"
        
        # Deze fields zijn private
        self.__id2 = 345
        self.__name2 = "RobinF"
        
    def display(self):
        print(self.__id2)
        print(self.__name2)
    
s = Student()
print(s.id)
print(s.name)

# Dit werkt niet!
'''
print(s.__id2)
print(s.__name2)
'''

# Op volgende manier oplossen
s.display()
# Of
print(s._Student__id2) # Dus niet volledig private!!