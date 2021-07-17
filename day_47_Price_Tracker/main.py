import requests
from my_conf import BROWSER_HEADERS, EMAIL, EMAIL_TO, PWD
from bs4 import BeautifulSoup
import smtplib
# import lxml

url = 'https://www.amazon.com/ASUS-i7-10750H-ScreenPad-Celestial-UX581LV-XS74T/dp/B08D941WH6/' \
      'ref=sr_1_1?dchild=1&keywords=ASUS%2BZenBook%2BPro%2BDuo%2BUX581&qid=1626358964&sr=8-1&th=1'
amzn_page = requests.get(url, headers=BROWSER_HEADERS).text
# with open('amzn.html', 'w') as f:
#     f.write(amzn_page)
soup = BeautifulSoup(amzn_page, 'lxml')
price = float(soup.find('span', id='priceblock_ourprice').getText()[1:].replace(',', ''))
title = soup.find('span', id='productTitle').getText().strip()
# print(price, title)
if price < 2620:
    msg = f'Subject:Amazon price alert!\n\n{title}\nnow ${price}\n{url}'
    with smtplib.SMTP('smtp.mail.yahoo.com') as conn:
        conn.starttls()
        conn.login(user=EMAIL, password=PWD)
        conn.sendmail(from_addr=EMAIL,
                      to_addrs=EMAIL_TO,
                      msg=msg.encode('utf-8'),)
