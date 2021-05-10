import datetime as dt
import pandas as pd
from random import randint
import smtplib
"""
##################### Extra Hard Version of Starting Project (No HINTS) ######################
1. Update the birthdays.csv
2. Check if today matches a birthday in the birthdays.csv
3. If step 2 is true, pick a random letter from letter templates 
   and replace the [NAME] with the person's actual name from birthdays.csv
4. Send the letter generated in step 3 to that person's email address.
"""
MY_NAME = 'Name'
EMAIL = 'mail@yahoo.com'
PWD = 'password'

now = dt.datetime.now()
today = now.day
month = now.month

df = pd.read_csv('birthdays.csv')
df = df[df.day == today]
df = df[df.month == month]

for i, row in df.iterrows():
    with open(f'letter_templates/letter_{randint(1, 3)}.txt') as f:
        letter = f.read().replace('[NAME]', row['name']).replace('[MY NAME]', MY_NAME)

    with smtplib.SMTP('smtp.mail.yahoo.com') as conn:
        conn.starttls()
        conn.login(user=EMAIL, password=PWD)
        conn.sendmail(from_addr=EMAIL,
                      to_addrs=row['email'],
                      msg=f"Subject:Happy Birthday!\n\n{letter}")
        print(f'A letter to {row["name"]} sent!')
