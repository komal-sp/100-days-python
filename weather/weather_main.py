import pandas
import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        temp = row[1]
        if temp != "temp":
            temperatures.append(int(temp))
        # print(row)
    print(temperatures)

# with open("weather_data.csv") as weather_data:
#     info = weather_data.readlines()
#     print(info)

data = pandas.read_csv("weather_data.csv")
print(data)