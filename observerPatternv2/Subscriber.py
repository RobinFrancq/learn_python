#https://www.youtube.com/watch?v=87MNuBgeg34
from Message import Message

# Subscriber of observer pattern
class Subscriber:
    def __init__(self, name):
        self.name = name
        self.data = Message()
    
    def update(self, message):
        self.data = message