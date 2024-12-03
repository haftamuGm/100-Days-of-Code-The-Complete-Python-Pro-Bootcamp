##################### Extra Hard Starting Project ######################
import random

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
import pandas
from smtplib import SMTP
import datetime as date
myemail="bsrathabtamu4@gmail.com"
password="cyvfqhsopaulzcfv"
data=pandas.read_csv("birthdays.csv")
now=date.datetime.now()
today=(now.month,now.day)
birthday={(data_row.month,data_row.day):data_row for (index,data_row) in data.iterrows()}
if today in birthday:
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    person=birthday[today]["name"]
    person_email=birthday[today]["email"]
    with open(file_path) as file:
        letter=file.read()
        letter=letter.replace("[NAME]",person)

        with SMTP("smtp.gmail.com") as con:
            con.starttls()
            con.login(user=myemail,password=password)
            con.sendmail(from_addr=myemail,
                         to_addrs=person_email,
                         msg=f"subject:BirthDay Wish\n\n{letter}")




