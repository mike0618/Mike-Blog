from datetime import datetime, timedelta
import requests
import smtplib
from my_config import EMAIL, EMAIL_TO, PWD, av_key, newsapi_key  # , auth_token, account_sid, twilio_phone, my_phone

# import os
# from twilio.rest import Client


def send_email(text):
    with smtplib.SMTP('smtp.mail.yahoo.com') as conn:
        conn.starttls()
        conn.login(user=EMAIL, password=PWD)
        conn.sendmail(from_addr=EMAIL,
                      to_addrs=EMAIL_TO,
                      msg=f"Subject:Share info\n\n{text}\n")


STOCK = 'TSLA'
COMPANY_NAME = 'Tesla Inc'
alphavantage = 'https://www.alphavantage.co/query'
av_prm = {'function': 'TIME_SERIES_DAILY',
          'symbol': STOCK,
          'outputsize': 'compact',
          'apikey': av_key}

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
resp = requests.get(alphavantage, params=av_prm)
resp.raise_for_status()

yesterday = datetime.now().date() - timedelta(days=1)
before_yesterday = datetime.now().date() - timedelta(days=2)

yesterday_close = float(resp.json()['Time Series (Daily)'][str(yesterday)]['4. close'])
before_yesterday_close = float(resp.json()['Time Series (Daily)'][str(before_yesterday)]['4. close'])

price_delta = yesterday_close - before_yesterday_close
percent_delta = 100 * price_delta / yesterday_close

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 2-3 news pieces for the COMPANY_NAME.
news_points = ['everything', 'top-headlines']
if abs(percent_delta) > 4:
    for point in news_points:
        newsapi = f'https://newsapi.org/v2/{point}'
        newsapi_prm = {'pageSize': 2,
                       # 'country': 'us',
                       'q': COMPANY_NAME,
                       'apiKey': newsapi_key, }

        resp = requests.get(newsapi, params=newsapi_prm)
        resp.raise_for_status()
        news = resp.json()['articles']  # list

        # STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number.
        for article in news:
            msg = f"Share info from {point}\n{STOCK}: {percent_delta:.2f}%\nHeadline: {article['title']}\n" \
                  f"Brief: {article['description']}\nPublished: {article['publishedAt']}"
            # client = Client(account_sid, auth_token)
            # message = client.messages.create(body=msg,
            #                                  from_=twilio_phone,
            #                                  to=my_phone)
            send_email(msg)
            print(msg)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required
 to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, 
 near the height of the coronavirus market crash.
or
TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required
 to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, 
 near the height of the coronavirus market crash.
"""
