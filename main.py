import requests
from bs4 import BeautifulSoup
import smtplib



MY_EMAIL = 'first.steps.coding@gmail.com'
MY_PASSWORD = 
URL ='https://www.amazon.co.uk/Philips-Cordless-attachments-Underarms-Technology/dp/B08Q8XTS51/ref=sr_1_2_sspa?crid=18M0V49GGMBQV&keywords=philips+lumea+ipl+9000+series&qid=1699089488&sprefix=philips+lumea+ipl+9000+series%2Caps%2C268&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
headers = {
  'accept-language': 'en-GB,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,en-US;q=0.6',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

response = requests.get(url= URL, headers= headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find(name='span', class_= 'a-price-whole')
price = int(str(price.text).replace('.', ''))
print(price)

if price >= 240:
  connection = smtplib.SMTP("smtp.gmail.com")
  connection.starttls()
  connection.login(user=MY_EMAIL, password=MY_PASSWORD)
  connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=MY_EMAIL,
    msg=f'Subject: Price is lower!\n\nThe price is now {price}. Go and check it out!'
  )
  connection.close()






