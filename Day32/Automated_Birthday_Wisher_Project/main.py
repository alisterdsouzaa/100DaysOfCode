import datetime as dt
import random
import pandas
import smtplib

My_Password = ""
My_Email = "alisterdsouzaa@outlook.com"

todays_month = dt.datetime.now().month
# print(todays_month)
todays_day = dt.datetime.now().day
# print(todays_day)

today_tuple = (todays_month, todays_day)

data = pandas.read_csv("birthdays.csv")
# print(data)

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(0, 5)}.txt"
    with open(file_path, "r") as file:
        content = file.read()
        replaced_content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.office365.com") as connection:
        connection.starttls()
        connection.login(My_Email, My_Password)
        connection.sendmail(from_addr=My_Email, to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{replaced_content}")
