# import csv

# data_list = []

# with open("day25/weather_data.csv") as data:
#     file_data = csv.reader(data)

#     temperature = []
#     for lines in file_data:
#         data_list.append(lines)
#         if lines[1] != "temp":
#             temperature.append(int(lines[1]))

# print(temperature)

# print(*data_list, sep="\n")

import pandas

data = pandas.read_csv("day25/weather_data.csv")
print(data["temp"])
