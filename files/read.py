import os, sys

# Nagaan of de file bestaat
if os.path.isfile("myfile.txt"):
    
    # Het lezen van een file (dat bestaat)
    f = open("myfile.txt", "r")
    
else:
    print("File does not exist")
    #sys.exit() om het programma af te sluiten
    sys.exit()
    
s = f.read()
print(s)
f.close()