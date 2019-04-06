import requests

from urllib2 import urlopen
my_ip = urlopen('http://ip.42.pl/raw').read()

print (my_ip)   

res = requests.get('http://api.ipstack.com/' +my_ip+ '?access_key=6a5c24ba7345dcaa0297c455341d5e3d&format=1')

data = res.json()

lat = data.get("latitude")
lon = data.get("longitude")

print(lat)
print(lon)