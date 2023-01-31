import pandas

squirrel_data = pandas.read_csv("./Day_25/Squirrel_census_data_analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

num_gray_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]["Primary Fur Color"])
num_cinnamon_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"])
num_black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]["Primary Fur Color"])

squirrel_colors = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [num_gray_squirrels, num_cinnamon_squirrels, num_black_squirrels]
}

squirrel_colors_data = pandas.DataFrame(squirrel_colors)
squirrel_colors_data.to_csv("./Day_25/Squirrel_census_data_analysis/squirrel_count.csv")