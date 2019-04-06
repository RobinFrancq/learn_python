class Objectcounter:
    
    numberOfObjects = 0
    
    def __init__(self):
        Objectcounter.numberOfObjects += 1
    
    # Aanduiden met decorator
    @staticmethod
    def displayCount():
        print(Objectcounter.numberOfObjects)

o1 = Objectcounter()
o2 = Objectcounter()

Objectcounter.displayCount()