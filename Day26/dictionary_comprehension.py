# Q1 Converting sentace to list and then creating dictionary
sentance = "Hi my name is Alister and I am learning dictionary comprehension"

each_word = sentance.split()
# print(each_word)

new_dict = {word: len(word) for word in each_word }
print(new_dict)


# Q2 Convert data from celc to Far
weather_c = {
    "Monday": 12,
    "Tuesday": 21,
    "Wednesday": 14,
    "Thursday": 23,
    "Friday": 22,
    "Saturday": 25,
    "Sunday": 11,
}

weather_f = {day: (value * 9/5) + 32 for (day, value) in weather_c.items()}
print(weather_f)
