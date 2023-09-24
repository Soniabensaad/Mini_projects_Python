import phonenumbers
#from test import number

from phonenumbers import geocoder
import folium

key = "from open cage API"
number = input("Enter phone number contry code: ")
ch_number = phonenumbers.parse(number, "CH")
Emplacement = (geocoder.description_for_number(ch_number, "en"))
print(Emplacement)

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))


from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(Emplacement)
result = geocoder.geocode(query)

latitude = result[0]['geometry']['lat']
longitude = result[0]['geometry']['lng']
print(latitude, longitude)


map_location = folium.Map(location = [latitude, longitude], zoom_start=15)
folium.Marker([latitude, longitude], popup=Emplacement).add_to(map_location)
map_location.save("mylocation.html")
