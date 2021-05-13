import requests
import smtplib
from time import sleep
from datetime import datetime
from my_config import mail_dict, EMAIL, PWD, owm_key, OWM_Endpoint


def dark():
    if sunrise < sunset:
        return hour_now < sunrise or hour_now > sunset
    else:
        return sunset < hour_now < sunrise


def send_email():
    with smtplib.SMTP('smtp.mail.yahoo.com') as conn:
        conn.starttls()
        conn.login(user=EMAIL, password=PWD)
        conn.sendmail(from_addr=EMAIL,
                      to_addrs=email,
                      msg=f"Subject:Look up!\n\nThe ISS is overhead right now!\n"
                          f"Time: {hour_now}:{minute_now}\n"
                          f"Latitude:{iss_lat}\nLongitude:{iss_lng}")


while True:
    sleep(1)
    st = 60 / len(mail_dict)
    for email, place in mail_dict.items():  # mail_dict: {email: (lat, lng),...}
        sleep(st + 1)
        lat = place[0]
        lng = place[1]

        now = datetime.now()
        hour_now = now.hour
        minute_now = now.minute

        w_prm = {'lat': lat,
                 'lon': lng,
                 'appid': owm_key,
                 'exclude': 'hourly,minutely,daily', }
        w_resp = requests.get(OWM_Endpoint, params=w_prm)
        w_resp.raise_for_status()
        w_data = w_resp.json()['current']
        sunrise = datetime.fromtimestamp(w_data['sunrise']).hour
        sunset = datetime.fromtimestamp(w_data['sunset']).hour
        w_id = int(w_data['weather'][0]['id'])
        # print(email, lat, lng, sunrise, hour_now, sunset, w_id)

        if dark() and w_id >= 800:
            iss_resp = requests.get(url="http://api.open-notify.org/iss-now.json")
            iss_resp.raise_for_status()
            data = iss_resp.json()
            iss_lat = float(data["iss_position"]["latitude"])
            iss_lng = float(data["iss_position"]["longitude"])

            if (lat - 5 <= iss_lat <= lat + 5) and (lng - 5 <= iss_lng <= lng + 5):
                print(f"Look up!👆 ISS is overhead right now!\n"
                      f"Time: {hour_now}:{minute_now}\n"
                      f"Latitude:{iss_lat}\nLongitude:{iss_lng}")
                send_email()
        #     else:
        #         print("The sky is clear and it's dark.\nWaiting for ISS...")
        # else:
        #     print("It's daytime yet... or the sky isn't clear.")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
