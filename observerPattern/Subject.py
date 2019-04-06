from abc import abstractmethod, ABCMeta

class Subject(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def register(self):
        pass
    
    @abstractmethod
    def unregister(self):
        pass
    
    @abstractmethod
    def notifyObservers(self):
        pass
    
    @abstractmethod
    def getUpdate(self, observerObj):
        pass