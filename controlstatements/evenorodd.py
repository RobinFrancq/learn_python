num = int(raw_input("Enter a number: "))

if num == 0:
    print("The the number is not even or odd")
elif num%2 == 0:
    print(str(num)+ " is even")
else:
    print(str(num)+ " is odd")