# Een decorator is een functie die een andere (inner) functie returnt 
def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner

# Met de @decor geef je aan dat deze functie als parameter gebruikt zal worden binnen de decor functie
@decor
def num():
    return 5

print(num())