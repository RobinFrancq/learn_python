import urllib, json
import requests 
from urllib2 import urlopen

class WeatherData:
    
    def __init__(self):
        
        #Get IP address
        my_ip = urlopen('http://ip.42.pl/raw').read()
        
        # Getting current location
        res = requests.get('http://api.ipstack.com/' +my_ip+ '?access_key=6a5c24ba7345dcaa0297c455341d5e3d&format=1')
        data = res.json()
        lat = str(data.get("latitude"))
        lon = str(data.get("longitude"))
        
        # Using the current location to retrieve the current weather
        url = "http://api.openweathermap.org/data/2.5/find?lat=" +lat+ "&lon=" +lon+ "&appid=75b6d925bab0543c7ed00f889aad883e"
        response = urllib.urlopen(url)
        locationName = json.loads(response.read()).get("list")[0].get("name")
        
        url = "http://api.openweathermap.org/data/2.5/weather?q=" +locationName+ "&appid=75b6d925bab0543c7ed00f889aad883e"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        
        # Senario when location is not found
        if data.get("message") != None:
            self.message = "NOT FOUND"
            
            self.country = None
            self.location = None
            self.lon = None
            self.lat = None
            
            self.desciption = None
            
            self.currentTemp = None
            self.minTemp = None
            self.maxTemp = None
            self.sunrise = None
            self.sunset = None
            self.imageName = None
            
            self.cloudPercentage = None
            
            self.pressure = None
            self.humidity = None
            
            self.windSpeed = None
            self.windDirection = None
        
        # Senario when location is found
        else:
            
            # Filling parameters by using the data from the API
            self.message = "FOUND"
            
            self.country = data.get("sys").get("country")
            self.location = data.get("name")
            self.lon = data.get("coord").get("lon")
            self.lat = data.get("coord").get("lat")
            
            self.desciption = data.get("weather")[0].get("main")
            self.preciseDescription = data.get("weather")[0].get("description")
            
            self.currentTemp = self.convertKToC(data.get("main").get("temp"))
            self.minTemp = data.get("main").get("temp_min")
            self.maxTemp = data.get("main").get("temp_max")
            self.sunrise = data.get("sys").get("sunrise")
            self.sunset = data.get("sys").get("sunset")
            
            if (self.desciption == "Thunderstorm"):
                self.imageName = "img/thunderstorm.gif"
            elif (self.desciption == "Drizzle"):
                self.imageName = "img/rain.gif"
            elif (self.desciption == "Rain"):
                if (self.preciseDescription == "light rain" or self.desciption == "moderate rain" or self.desciption == "light intensity shower rain"):
                    self.imageName = "img/rain.gif"
                else:
                    self.imageName = "img/shouwer_rain.gif"
            elif (self.desciption == "Snow"):
                self.imageName = "img/snow.gif"
            elif (self.desciption == "Atmosphere"):
                self.imageName = "img/scattered_clouds.gif"
            elif (self.desciption == "Clear"):
                self.imageName = "img/clear_sky.gif"
            elif (self.desciption == "Clouds"):
                if (self.preciseDescription == "few clouds"):
                    self.imageName = "img/few_clouds.gif"
                elif (self.preciseDescription == "scattered clouds"):
                    self.imageName = "img/scattered_clouds.gif"
                elif (self.preciseDescription == "broken clouds" or self.preciseDescription == "overcast clouds"):
                    self.imageName = "img/broken_clouds.gif"
                
            self.cloudPercentage = data.get("clouds").get("all")
            
            self.pressure = data.get("main").get("pressure")
            self.humidity = data.get("main").get("humidity")
            
            self.windSpeed = data.get("wind").get("speed")
            self.windDirection = data.get("wind").get("deg")
    
    # Methode to convert Kelvin to Celcius        
    def convertKToC(self, Ktemp):
        temp = float(Ktemp)-272.15
        temp = int(temp)
        temp = str(temp)
        return temp
    