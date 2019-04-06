# Een functie in een functie
# De functie "message" is niet beschikbaar buiten de functie "display"!
def display(name):
    def message():
        return "Hello"
    result = message()+ " " +name
    return result

print(display("Robin"))