import requests
from bs4 import BeautifulSoup
import smtplib
import time
#Enter any product URL, this is just an example link
URL = "https://www.amazon.in/Samsung-Galaxy-Space-Black-Storage/dp/B07HGN617M/ref=sr_1_1_sspa?dchild=1&keywords=samsung+m31s&qid=1596708615&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFQNVBLQzFLTlpGWSZlbmNyeXB0ZWRJZD1BMDEwNDk5ODNLQklINUFNVUJaMDYmZW5jcnlwdGVkQWRJZD1BMDc1MDMzMjI5UFk2U1lLV0M4N0Umd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
#Price checking
def check():
    product = requests.get(URL, headers = header)

    soup = BeautifulSoup(product.content,'html.parser')

    title = soup.find(id = "title_feature_div").get_text() 
    price = soup.find(id = "priceblock_dealprice").get_text()
    roundup = price[0:8]
    #This whole process of stripping was done to reduce the price to just a simple integer
    roundup1 = roundup.strip('₹')
    roundup2 = roundup1.replace(',','')
    roundup3 = roundup2.strip()
    roundup4=int(roundup3)
    print(roundup3)
    print(title.strip())
#Enter any number that you have to reduce to
    if (roundup4 < 18000):
        send_email()
def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() #acknowledges connection between sender and receiver
    server.starttls() #Encrypted connection
    server.ehlo()
    server.login('','')

    alert = 'The price just went down! Grab it before it is gone'
    link = 'https://www.amazon.in/Samsung-Galaxy-Space-Black-Storage/dp/B07HGN617M/ref=sr_1_1_sspa?dchild=1&keywords=samsung+m31s&qid=1596708615&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFQNVBLQzFLTlpGWSZlbmNyeXB0ZWRJZD1BMDEwNDk5ODNLQklINUFNVUJaMDYmZW5jcnlwdGVkQWRJZD1BMDc1MDMzMjI5UFk2U1lLV0M4N0Umd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

    message = f"Subject: {alert}\n\n{link}"


    server.sendmail(
        #sender's email
        '',
        #receiver's email
        '',
        message
    )

    print('Email sent succesfully!')
    server.quit()
while(True):
    check()
    time.sleep(60 * 60)