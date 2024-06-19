""" 
Open weather app retrieves information about the weather on a given day from 1979 onwards.

Could make an app that produces a first person monologue or diary entry from an individual on a given day in history.
The weather will be described in detail and the individual will talk about their day.

Underneith there will be a mock advert which mimics the "hot women near you" as the IP of the user is pulled.
But instead it will be a "Adorable dogs near you" with a picture of a dog and a button to adopt it.
    It will say "within 10 miles of {your location}"

API's used here
    OpenAI > Check email
    OpenWeather > https://openweathermap.org/api
    DogsCEO > https://thedogapi.com/

How to create the front end?
    Flask? Django?
    HTML, CSS, JS
        Still lost on JS, not done anything on there yet.
"""

# See if I can create something with just python for now.

# Open weather api key 

import requests
import time

# Define your parameters
lat = "37.7749"  # Latitude of San Francisco, for example
lon = "-122.4194"  # Longitude of San Francisco, for example
api_key = ""

# Define the date and time you want to query in UNIX timestamp format
dt = int(time.mktime(time.strptime('2023-06-01', '%Y-%m-%d')))

# Construct the URL
url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=39.099724&lon=-94.578331&dt=1643803200&appid={api_key}"

# Make the request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
    # This will be output since I will need a different subscription service to access historical data.
    # https://openweathermap.org/price#history
