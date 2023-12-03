from datetime import datetime
import requests

MY_LAT = 17.385044
MY_LNG = 78.486671

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted":0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])


#print(f"sunrise: {sunrise},sunset: {sunset} at Hyderabad")

time_now = datetime.now()
#print(time_now)
print(time_now.hour)