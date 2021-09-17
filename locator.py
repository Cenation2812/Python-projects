import geopy
from geopy.geocoders import Nominatim

address=input("Enter your destination:")
geolocator = Nominatim(user_agent="Shourjadeep")
location = geolocator.geocode(address)
print(location.address)
print((location.latitude, location.longitude))
