#Numeric types
a=13
b=100
c=-66
print(a, b, c)

#Floating points types
x=33.5
y=-25.8
z=205.0 #Dit neemt Python aan als floating point omdat er 205.0 staat (wat eigenlijk gelijk is aan 205)
print(x, y, z)

#Nagaan van welk type een variabele is
print(type(a))
print(type(z))

#Complex types
d=3+5j
print(type(d))

#Binary types
e=0B1010
print(e) #Geeft de binaire waarde weer in decimale vorm 
print(type(e)) #Geprint wordt een benaire waarde als integer aanzien!

#Hexadecimale types
f=0XFF
print(f) #Geeft de hexadecimale waarde weer in decimale vorm
print(type(f)) #Geprint wordt een hexadecimale waarde als integer aanzien!

#Boolean types
g=True
print(type(g))
print(9>8) #Een expressie print een boolean af

#CONVERTEREN VAN NUMMERIEKE TYPES
h=int(x) #Boolean --> Integer (afronding altijd naar beneden)
print(h)
print(type(h))

i=float("22.5") #String --> Floating point
print(i)
print(type(i))

print(bin(10)) #Integer --> Binair
print(hex(10)) #Integer --> Hexadecimal
