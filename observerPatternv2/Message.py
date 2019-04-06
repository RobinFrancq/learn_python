from datetime import datetime
from WeatherData import WeatherData

# Message that contains methodes to retrieve data (for the observer)
class Message:
    
    def __init__(self):
        self.time = self.getCurrentTime()
        self.date = self.getCurrentDate()
        self.weather = self.getWeather()
        self.mainMessage = self.getMainMessage()
        
    def getCurrentTime(self):
        return str(datetime.now().strftime('%H:%M'))
    
    def getCurrentDate(self):
        return str(datetime.now().strftime('%d/%m/%Y'))
    
    def getWeather(self):
        weather = WeatherData()
        return weather
    
    def getMainMessage(self):
        message = ""
        hour = self.getCurrentTime()[0:2]
        hour = int(hour)
        if (0 <= hour < 12):
            message = "Good Morning"
        elif (12 <= hour < 17):
            message = "Good Afternoon"
        elif (17 <= hour <= 23):
            message = "Good Evening"
        return (message)