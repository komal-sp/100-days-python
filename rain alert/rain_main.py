from twilio.rest import Client
import requests

account_sid = "ACfbbea5bbf3d45bf4d3ae3acd4f61f263"
auth_token = "a6fd8dc9a96eb2d6192b36e135681bad"

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "dea4a9a6af8d6e18b13d16cef6694c6f"
weather_params = {
    "lat": 13.072090,
    "lon": 80.201859,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.status_code
weather_data = response.json()
print(weather_data)
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_='+13167126934',
        to='+919075206823'
    )
    print(message.status)
