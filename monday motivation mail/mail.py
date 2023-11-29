# import smtplib
# my_email = "blossom.diaries29@gmail.com"
# password = "wyoc dsvz nmmx iypx"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="ksphadtare54@gmail.com",
#                         msg="Subject:Birthday Wish\n\nThis is the body of my email.")
# #connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()
print(year, month, day)

date_of_birth = dt.datetime(year=1998, month=12, day=29, hour=8)