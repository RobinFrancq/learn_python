# open de file om naar te schrijven 
f = open("myfile.txt", "w")

print("Enter Text (Type # when you are done)")

# While loop zolang de gebruiker gaan # heeft ingedrukt
s = ""
while s != "#":
    s = raw_input()
    
    # Schrijven naar de gemaakte file
    f.write(s+"\n")

# Het sluiten van de file --> niet vergeten!
f.close()