# Pandas module. Data Frames and Data Series
import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data)

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # find avg temp in list of temp
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
#
# print(data["temp"].max())
#
# # Get data in columns
# print(data.condition)

# Get data in Row
a = data[data.day == "Monday"]
# print(a)

# print(data[data.temp == data.temp.max()])

# def cel_far(temp):
#     return (9 / 5 * temp) + 35
#
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# temp_far = cel_far(monday_temp)
# print(temp_far)

# Creating data frame from scratch
data_dict = {
    "student": ["alister", "kacey", "eve"],
    "marks": [35, 100, 99]
}

student_data = pd.DataFrame(data_dict)
print(student_data)
# saving this data to a csv file.
student_data.to_csv("new_data_file.csv")
