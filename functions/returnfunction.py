# Het returnen van een functie
def display():
    def message():
        return "Hello"
    
    return message

fun = display()
print(fun())