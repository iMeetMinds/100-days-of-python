import smtplib
import datetime as dt
import random
import Dummy

now = dt.datetime.now()
today_day = now.weekday()

my_email = Dummy.MY_EMAIL
my_pass = Dummy.MY_PASS

if today_day == 6:

    with open("quotes.txt","r") as quotes:
        quotes_list = quotes.read()
        quotes_list = quotes_list.split('\n')
        quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=Dummy.TO_EMAIL,
            msg=f"Subject:Monday Motivation \n\n{quote}"
        )