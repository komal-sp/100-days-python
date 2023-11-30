import random
import smtplib
import datetime as dt

MY_EMAIL = "blossom.diaries29@gmail.com"
PASSWORD = "wyoc dsvz nmmx iypx"

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        # connection.sendmail(from_addr=MY_EMAIL, to_addrs="Papiyatiwari1999@gmail.com",
        #                     msg=f"Subject:Monday Motivation\n\n{quote1}")
        # connection.sendmail(from_addr=MY_EMAIL, to_addrs="papiyatiwari06051999@gmail.com",
        #                     msg=f"Subject:Monday Motivation\n\n{quote2}")
        print(quote)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="blossom.diaries29@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="vaibhavghadage22@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")