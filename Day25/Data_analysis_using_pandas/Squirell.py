import pandas
# Extract count of squirrel count and export to a new csv file

# read csv
data = pandas.read_csv("2018_Central-Park-Squirrel-Census-Squirrel-Data.csv")

grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrel)

data_dict = {
    "fur colour": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel, red_squirrel, black_squirrel]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")
