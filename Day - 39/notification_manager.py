import smtplib

import Dummy
import constants as const


class NotificationManager:

    def __init__(self):
        pass

    def send_mail(self, flight_data, destination_place):

        segments = flight_data['itineraries'][0]['segments']
        email_content = (f"Low Price Alert!! \n\n Only ${flight_data['price']['total']} to fly from "
                         f"{const.CURRENT_PLACE}-{segments[0]['departure']['iataCode']}"
                         f" to {destination_place}-{segments[-1]['arrival']['iataCode']}"
                         f", from {segments[0]['departure']['at']} to {segments[-1]['arrival']['at']}")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=Dummy.MY_EMAIL, password=Dummy.MY_PASS)
            connection.sendmail(
                from_addr=Dummy.MY_EMAIL,
                to_addrs=Dummy.TO_EMAIL,
                msg=f"Subject : Low Price Alert on Flight Booking!! \n\n {email_content}"
            )