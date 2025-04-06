import requests
import datetime as dt
import smtplib
import Dummy
import time

MY_LAT = 33.5515
MY_LNG = -87.2088

def is_iss_near():
    global MY_LNG,MY_LAT
    response_iss = requests.get(url='http://api.open-notify.org/iss-now.json')
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss['iss_position']['latitude'])
    iss_longitude = float(data_iss['iss_position']['longitude'])

    if (iss_longitude <= (MY_LNG + 5) or iss_longitude >= (MY_LNG - 5)) and (iss_latitude <= (MY_LAT + 5) or iss_latitude >= (MY_LAT - 5)):
        return True
    else:
        return False


def is_night():
    parameter = {
        'lat' : MY_LAT,
        'lng' : MY_LNG,
        'formatted' : 0
    }
    response = requests.get(url=' https://api.sunrise-sunset.org/json', params=parameter)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    print(sunset)

    time_now = dt.datetime.now()
    time_hour = time_now.hour

    return sunset < time_hour

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=Dummy.MY_EMAIL, password=Dummy.MY_PASS)
        connection.sendmail(
            from_addr=Dummy.MY_EMAIL,
            to_addrs=Dummy.TO_EMAIL,
            msg="Subject:Look Up \n\n ISS is above you. Look up!!"
        )

while True:
    time.sleep(60)
    if is_iss_near() and is_night():
        send_mail()