import smtplib
import datetime as dt
import random
import pandas
import Dummy
##################### Extra Hard Starting Project ######################
MY_EMAIL = Dummy.MY_EMAIL
MY_PASS = Dummy.MY_PASS

# 1. Update the birthdays.csv
bday_file = pandas.read_csv("birthdays.csv")
bday_dir = bday_file.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

bday_list = [dit for dit in bday_dir if dit['month'] == month and dit['day'] == day]

def send_email(letter):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=Dummy.TO_EMAIL,
            msg=f"Subject:Happy Birthday!! \n\n{letter}"
        )
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for dirct in bday_list:
    letter_no = random.randint(1,3)
    with open(f"letter_templates/letter_{letter_no}.txt", mode="r") as letter_file:
        proper_letter = letter_file.read().replace("[NAME]", dirct['name'])
        send_email(proper_letter)

# 4. Send the letter generated in step 3 to that person's email address.




