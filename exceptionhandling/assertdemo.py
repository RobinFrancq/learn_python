# Assert handeling
try:
    num = int(raw_input("Enter a even number: "))
    assert num%2==0, "You have entered a invalid input or odd number"
except AssertionError as obj:
    print(obj)

print("Code after assertion")
    