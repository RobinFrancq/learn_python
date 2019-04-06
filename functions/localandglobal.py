x=123

def display():
    x=678
    print(x)
    
    # Een globale variabele aanspreken (handig indien globale en local variabele dezelfde naam hebben)
    print(globals()['x'])

print(x)
display()

# Een functie toekennen aan een variabele
z = display
z()