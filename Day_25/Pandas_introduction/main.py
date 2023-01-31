""" with open("./Day_25/weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
 """

""" import csv

with open("./Day_25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures) """

from numpy import average
import pandas

data = pandas.read_csv("./Day_25/weather_data.csv")
#print(data["temp"])
""" data_dict = data.to_dict()
print(data_dict)

data_list = data["temp"].to_list()
print(data_list)

average = 0
for data in data_list:
    average += data / len(data_list)
print(average)

average = sum(data_list) / len(data_list)
print(average) """

""" average = data["temp"].mean()
print(average)

maximum = data["temp"].max()
print(maximum)

print(data.condition)
 """
""" print(data[data.day == "Monday"]) 
print(data[data.temp == data.temp.max()])
 """
""" monday = data[data.day == "Monday"]
temp_on_monday = (int(monday.temp) * 1.8) + 32
print(temp_on_monday)
 """

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("./Day_25/new_data.csv")