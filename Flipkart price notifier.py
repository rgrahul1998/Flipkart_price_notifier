from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

count = 0
product_link = input('Link of the product you to get notified for price drop \n')
phone_no = input('enter your phone number including country code that you want to get notified on \n')
expected_price = int(input('enter expected price: \n'))

header = {'User-Agent':input('enter User Agent \n')}
account_sid = input('enter twilio account SID \n')
token = input('enter twilio auth token \n')
twilio_phone_no = input('enter twilio phone number \n')


try:
    request = requests.get(product_link, headers=header)
    print(request)
    request.raise_for_status()

    soup = BeautifulSoup(request.text, 'html.parser')
    price = float(soup.find('div', class_="_30jeq3 _16Jk6d").text.replace(',', '').replace('₹', ''))
    product_name = soup.find('span', class_='B_NuCI').text
    print (price)
    print (product_name)

    if price <= expected_price:
        client = Client(account_sid, token)
        message = client.messages.create(from_=twilio_phone_no, body=(f'There is a price drop of {product_name}. Click on {product_link} to purchase'), to=phone_no)
        print ('person has been notified')
    else:
            pass

except Exception as e:
    print (Exception)