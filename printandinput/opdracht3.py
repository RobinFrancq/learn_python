num = int(raw_input("Enter a number: "));

primeFlag = True;

for x in range(2, num):
    if(num%x == 0):
        primeFlag = False

if(primeFlag):
    print("Prime Number!")
else:
    print('Not a Prime Number')