import requests
from datetime import datetime
import smtplib


MY_LAT = 53.392658 #latitude
MY_LONG = -2.587000 # longitude
my_email="aman.sharma617c@gmail.com"
my_password="yzzdzgrlftisfxlz"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


close=False
#position is within +5 or -5 degrees of the ISS position.
if iss_longitude > MY_LONG-5 or iss_longitude<MY_LONG+5 and iss_latitude > MY_LAT-5 or iss_latitude<MY_LAT+5:
    close=True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()


if close and time_now.hour>=sunset:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Look UP!!\n\n It's dark and you can see ISS")




