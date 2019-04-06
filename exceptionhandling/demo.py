import logging

# instellen van de logger (naar een file + level)
logging.basicConfig(filename="mylog.log", level=logging.DEBUG)

# Exception handeling
try:
    # File API (zie later)
    f = open("myfile", "w")
    a,b = [int(x) for x in raw_input("Enter two numbers: ").split()]
    logging.info("Division in progress")
    c = a/b
    f.write("Writing %d into file" %c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")
    logging.error("Division by zero")
else:
    print("You have antered a non zero number")
finally:
    f.close()
    print("File closed")
    
print("Code after the exception")
    