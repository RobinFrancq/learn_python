import re

str = "Take 1 up 1-3-2019 one idea. One 23 idea 45 at a time Only 12-11-2020"

# regular expressions starten met 'r'
# deze zoekt substrings dat starten met o en gevolgd worden door 2 willekeurige characters
# een regular expression returnt een substring (de eerste die gevonden wordt)
result = re.search(r'o\w\w', str)
# group() wordt gebruikt voor de search-functie op re
# OPM: indien result == None dan kan group() niet gebruikt worden (je krijgt dus een error)
print(result.group())

# returnt een list
result = re.findall(r'o\w\w', str)
print(result)

# match zoekt enkel in het begin van de string (dus in onderstaand geval None dus error)
result = re.match(r'O\w\w', str)
#print(result.group())

# split verdeeld de string in afzonderlijke substrings
# In dit geval: verdeel string in afzonderlijke substrings (afhankelijk van de een digit)
result = re.split(r'\d+', str)
print(result)

# veranderen van een substring door een andere substring
result = re.sub(r'one', 'two', str)
print(result)

# een of meer characters
result = re.findall(r'O\w+', str)
print(result)

# 0 of meer characters
result = re.findall(r'O\w*', str)
print(result)

# 0 of 1 character
result = re.findall(r'O\w?', str)
print(result)

# precies 3 character
result = re.findall(r'O\w{3}', str)
print(result)

# minimum 1 maximun 2
result = re.findall(r'O\w{1, 2}', str)
print(result)

# Zoeken naar een datum
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(result)

# ^ is aan het begin van de string
result = re.search(r'^T\w*', str)
print(result.group())


