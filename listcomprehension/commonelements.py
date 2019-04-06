a=[2, 4, 6, 8]
b=[1, 2, 3, 4]

# Gewone manier
'''
result=[]
for i in a:
    if i in b:
        result.append(i)

print(result)
'''

# Met lst comprehention
result=[i for i in a if i in b]
print(result)