# Bytes
lst=[20, 30, 40, 234]
print(type(lst))

b=bytes(lst)
print(type(b)) #Type wordt STR wat volgens mij bytes wilt zeggen

# b[3] = 22 --> ERROR (bytes kan geen assignment doen)

# Bytearray
b1=bytearray(lst)
print(type(b1))

b1[2] = 33
