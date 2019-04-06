from abc import abstractmethod, ABCMeta

class TouchScreenLaptop(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def scroll(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
    __metaclass__ = ABCMeta
    
    def scroll(self):
        print("HP is Scrolling")
    
    @abstractmethod
    def click(self):
        pass

class DELL(TouchScreenLaptop):
    __metaclass__ = ABCMeta
    
    def scroll(self):
        print("DELL is Scrolling")
    
    @abstractmethod
    def click(self):
        pass

class HPNotebook(HP):
    
    def click(self):
        print("HPNotebook is clicking")
        
class DELLNotebook(DELL):
    
    def click(self):
        print("DELLNotebook is clicking")


laptop = HPNotebook()
laptop.click()
laptop.scroll()

laptop2 = DELLNotebook()
laptop2.click()
laptop2.scroll()