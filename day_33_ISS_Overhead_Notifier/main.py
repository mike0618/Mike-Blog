import requests
import smtplib
from time import sleep
from datetime import datetime, timezone
from config import MY_LAT, MY_LNG, EMAIL, EMAIL_TO, PWD, parameters

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise, sunset)


def dark():
    hour_now = datetime.now(timezone.utc).hour
    if sunrise < sunset:
        return hour_now < sunrise or hour_now > sunset
    else:
        return sunset < hour_now < sunrise


def send_email():
    with smtplib.SMTP('smtp.mail.yahoo.com') as conn:
        conn.starttls()
        conn.login(user=EMAIL, password=PWD)
        conn.sendmail(from_addr=EMAIL,
                      to_addrs=EMAIL_TO,
                      msg=f"Subject:Look up!👆\n\nISS is overhead right now!\n"
                          f"lat:{iss_latitude}\nlng:{iss_longitude}")


while True:
    sleep(60)
    if dark():
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LNG - 5 <= iss_longitude <= MY_LNG + 5):
            print(f"Look up!👆 ISS is overhead right now!\n"
                  f"lat:{iss_latitude}\nlng:{iss_longitude}")
            send_email()
        else:
            print("It's dark already. Waiting for ISS...")
    # else:
    #     print("It's daytime yet...")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
