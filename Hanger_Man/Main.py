import random
import urllib, json 
from Player import Player

url = "https://raw.githubusercontent.com/words/an-array-of-english-words/master/words.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
p1 = Player(data[random.randint(1,len(data))])
hasWon = False

print("----------- WELCOME TO HANGMAN -----------")
print("\nThe CPU will pick a word...\n")

while True:
    while p1.state >= 1:
        print("\n" +p1.displayWordStatus())
        
        char = raw_input("Make a guess: ")
        
        if p1.checkIfLetterIsInWordAndUpdate(char):
            print("Correct!")
        else:
            print("Not Correct!")
        
        if p1.checkIfWordIsFound():
            hasWon = True
            break
    
    if hasWon == True:
        print("\nYOU WON!!\n")
        print("Right Answer Was: " +p1.word)
        
        # Refresh player
        print("\nThe CPU will pick a word...\n")
        p1 = Player(data[random.randint(1,len(data))])
        hasWon = False
    else:
        print("\nYOU ARE DEAD!!\n")
        print("Right Answer Was: " +p1.word)
        
        # Refresh player
        print("\nThe CPU will pick a word...\n")
        p1 = Player(data[random.randint(1,len(data))])
        hasWon = False