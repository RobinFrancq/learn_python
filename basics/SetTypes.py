# Set Type (laat geen duplicate toe en houd geen rekening met volgorde, dus geen indexing)
s={10, 20, 30, "xyz", 10, 20, 10}
print(s)
print(type(s))

# Toevoegen en verwijderen van elementen
s.update([88, 99])
print(s)

# print(s[0]) --> ERROR
# print(s[0:5]) --> ERROR
# print(s*3) --> ERROR

s.remove(30)
print(s)

f=frozenset(s) # Maakt een set frozen
# f.update([20]) --> ERROR
# f.remove(20) --> ERROR