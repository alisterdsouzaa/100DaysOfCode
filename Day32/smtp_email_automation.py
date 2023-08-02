# # SMTP --> Simple mail transfer protocol
# # TLS --> Transfer Layer Security
#
import smtplib
import datetime as dt
import random

password = "" # Use email password
email = ""  # use email to run the program sucessfully

now = dt.datetime.now()
weekday = now.weekday()

list_of_quotes = []

if weekday == 0:
    # Opening file and selecting a random quote.
    with open("quotes.txt", "r") as file:
        for line in file:
            list_of_quotes.append(line)

random_quote = random.choice(list_of_quotes)
print(random_quote)


# Using SMTP lib module to send emails
with smtplib.SMTP("smtp.gmail.com") as connection:  # Make sure your email providers SMTP is correct
    connection.starttls()  # Starts Transfer Layer Security
    connection.login(user=email, password=password)  # Logged in using email and password.
    connection.sendmail(from_addr=email,
                        to_addrs="alisterdsouzaa@outlook.com",
                        msg="Subject: Here is your monday motivation using python\n\n"
                            f"{random_quote}")
