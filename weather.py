#Zach Gerken
#Chapter 9 Lab 3
#November 9 2022
import requests

zip_code = input("What is your zip code?: ")

# https://api.openweathermap.org/data/2.5/weather?zip=43545,us&appid=4f777cede41381c2655590f7a7202133&units=imperial
response = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=" + zip_code + ",us&appid=4f777cede41381c2655590f7a7202133&units=imperial")

if response:
   response_dict = response.json()
   conditions = response_dict["weather"]
   print("Current Weather for",response_dict["name"])
   print("Temperature:", response_dict["main"]["temp"])
   print("Feels Like:", response_dict["main"]["feels_like"])
   print("Humidity:", response_dict["main"]["humidity"])
   print("Wind:", response_dict["wind"]["speed"], "knots from", response_dict["wind"]["deg"], "degrees")


