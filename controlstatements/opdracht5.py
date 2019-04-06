num = int(raw_input("Enter a number: "))

for x in range(1, num+1):
    if (x > 100):
        break
    elif (x%10 == 0):
        continue
    else:
        print(x)
        