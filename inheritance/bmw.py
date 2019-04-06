from abc import abstractmethod, ABCMeta

# Een interface
class BMW(object):
    # Dit gebruiken om aan te geven dat abstract klassen overwrite moeten worden!
    __metaclass__ = ABCMeta
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @abstractmethod  
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
        
    # Abstract methodes (childs moeten dit implementeren)
    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):
    
    def __init__(self, crouseControlEnable, make, model, year):
        # Een manier
        # BMW.__init__(self, make, model, year)
        
        # Andere manier (Python 3)
        super(ThreeSeries, self).__init__(make, model, year)
        self.crouseControlEnable = crouseControlEnable
        
    def display(self):
        print(self.crouseControlEnable)
    
    # Overwriting
    def start(self):
        # Parent methods kunnen ook aangesproken worden
        super(ThreeSeries, self).start()
        print("Button Start")
    
    def stop(self):
        # Parent methods kunnen ook aangesproken worden
        super(ThreeSeries, self).stop()
        print("Button Stop")
    
    def drive(self):
        print("Three Series is being driven")

class FiveSeries(BMW):
    
    def __init__(self, parkingAssistEnabled, make, model, year):
        super(FiveSeries, self).__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled
        
    # Overwriting
    def start(self):
        # Parent methods kunnen ook aangesproken worden
        super(FiveSeries, self).start()
        print("Remote Start")
    
    def stop(self):
        # Parent methods kunnen ook aangesproken worden
        super(FiveSeries, self).stop()
        print("Remote Stop")
        
    def drive(self):
        print("Five Series is being driven")

# OPM: Polimorfisme is automatisch dynamisch at runtime in Python!
threeSeries = ThreeSeries(True, "BMW", "328i", "2018")
print(threeSeries.crouseControlEnable)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()