class Patient:
    
    def setId(self, myId):
        self.id = myId
    def setName(self, name):
        self.name = name
    def setSsn(self, ssn):
        self.ssn = ssn
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getSsn(self):
        return self.ssn

p1 = Patient()

p1.setId(1)
p1.setName("John")
p1.setSsn(1)

print(p1.getId())
print(p1.getName())
print(p1.getSsn())