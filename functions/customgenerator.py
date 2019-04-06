# Yield gaat een result opslaan in memorie en op het einde pas vrijgeven
def customdef(x,y):
    while x<y:
        yield x
        x+=1
        
result = customdef(20, 30)

for i in result:
    print(i)