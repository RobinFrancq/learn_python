def average(a=10, b=20):
    print(a)
    print(b)
    return (a+b)/2

# Keyword arguments worden hier gebruikt
result = average(b=10, a=20)
print(result)

# Door default parameters werkt volgende toch
print(average(a=30))