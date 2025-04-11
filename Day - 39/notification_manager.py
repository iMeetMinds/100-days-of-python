import smtplib

import Dummy



class NotificationManager:

    def __init__(self):
        pass

    def send_mail(self, email_content):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=Dummy.MY_EMAIL, password=Dummy.MY_PASS)
            connection.sendmail(
                from_addr=Dummy.MY_EMAIL,
                to_addrs=Dummy.TO_EMAIL,
                msg=f"Subject : Low Price Alert on Flight Booking!! \n\n {email_content}"
            )