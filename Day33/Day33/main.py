import requests
import datetime
import time
from smtplib import SMTP
MY_LAN=9.033138
MY_LONG=38.750077

myemail="bsrathabtamu4@gmail.com"
password="cyvfqhsopaulzcfv"
def is_iss_overhead():
    iss_location=requests.get("http://api.open-notify.org/iss-now.json")
    iss_longitude=float(iss_location.json()["iss_position"]["longitude"])
    iss_latitude=float(iss_location.json()["iss_position"]["latitude"])

    if MY_LAN - 5 <= iss_latitude >= MY_LAN + 5 and MY_LONG - 5.0 <= iss_longitude <= MY_LONG + 5:
        return True
def is_night():
    parameter={
        "lat":MY_LAN,
        "lng":MY_LONG,
        "formatted":0,
    }
    result=requests.get(" https://api.sunrise-sunset.org/json",params=parameter)
    result.raise_for_status()
    sunrise=int(result.json()['results']['sunrise'].split('T')[1].split(':')[0])
    sunset=int(result.json()['results']['sunset'].split('T')[1].split(':')[0])
    time_now=datetime.datetime.now().hour
    if time_now<sunset or time_now>sunrise:
        return True

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        with SMTP("smtp.gmail.com") as conection:
            conection.starttls()
            conection.login(user=myemail,password=password)
            conection.sendmail(from_addr=myemail,
                               to_addrs="habtamugm16@gmail.com",
                               msg="subject:Look up\n\n The ISS is above you in The Sky")



