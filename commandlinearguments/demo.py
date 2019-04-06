# Importeren van sys waar commandline arguments in zitten
import sys

# argv zijn alle commandline arguments binnen sys
lst=sys.argv

# Onder Run Configurations kan je argumenten meegegeven
# In console is dit "Python demo.py 123 456 789"
for i in lst:
    print (i)

print(len(lst))

print(lst[0])