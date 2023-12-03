import time
from datetime import datetime
import requests
import smtplib

MY_EMAIL = "blossom.diaries29@gmail.com"
PASSWORD = "wyoc dsvz nmmx iypx"
MY_LAT = 17.385044
MY_LNG = 78.486671


def iss_iss_overhead():
    iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss.raise_for_status()
    iss_data = iss.json()

    iss_latitude = iss_data["iss_position"]["latitude"]
    iss_longitude = iss_data["iss_position"]["longitude"]

    # Your position is within +5 and -5 degrees of the iss position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if  iss_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look up☝️\n\nThe ISS is above you in the sky."
        )
