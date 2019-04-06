class Product:
    
    # Default Constructor (maakt de properties rechtstreeks aan)
    def __init__(self):
        self.name = 'IPhone'
        self.description = 'A Phone'
        self.price = 999
    
    # Methode    
    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)
        
# Gebruik van de klasse (gebruik van constructor)
p1 = Product()
p1.display()

p2 = Product()
p2.display()