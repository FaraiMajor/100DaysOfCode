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

# data = pandas.read_csv("day25/weather_data.csv")
# print(data)
# print(data["temp"]) or data.temp

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temp = sum(temp_list) / len(temp_list)
# print(f"average: {avg_temp}")

# print(data["temp"].mean ())

# get data in a row

# print(data[data.day == "Monday"])

# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32


# # create a dataframe from scratch

# data_dict = {
#     "students": ["Any", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("day25/new_data.csv")

data = pandas.read_csv(
    "day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]

}

d_frame = pandas.DataFrame(data_dict)
d_frame.to_csv("day25/squirrel_count.csv")
