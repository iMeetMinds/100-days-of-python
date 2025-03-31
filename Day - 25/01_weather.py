# with open("./weather-data.csv") as weather_data:
#     content = weather_data.readlines()
#     print(content)

# import csv
#
# with open("./weather-data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in list(data)[1:]:
#         temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data  = pandas.read_csv("./weather-data.csv")
# print(data)

# temp_data = data['temp'].to_list()
# avg_temp = sum(temp_data)/len(temp_data)
# print(avg_temp)

print(data["temp"].mean())

print(data["temp"].max())

print(data[data.temp == data.temp.max()])