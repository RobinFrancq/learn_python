numberLst = [int(x) for x in raw_input("Enter three numbers seperated by space: ").split()]

numberCount = 3.0;
numberSum = 0;

for num in numberLst:
    numberSum += num

avg = float(numberSum)/numberCount

print(avg)