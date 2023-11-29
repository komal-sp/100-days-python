import random
import smtplib
import datetime as dt

MY_EMAIL = "blossom.diaries29@gmail.com"
PASSWORD = "wyoc dsvz nmmx iypx"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote1 = random.choice(all_quotes)
        quote2 = random.choice(all_quotes)

    print(quote1)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        # connection.sendmail(from_addr=MY_EMAIL, to_addrs="Papiyatiwari1999@gmail.com",
        #                     msg=f"Subject:Monday Motivation\n\n{quote1}")
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="papiyatiwari06051999@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote2}")