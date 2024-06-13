import requests
from bs4 import BeautifulSoup
import time
import random
import csv

# save in csv file
file = open('socks.csv', 'w', encoding='utf-8_sig', newline='\n')
wr_obj = csv.writer(file)
wr_obj.writerow(['Name', 'Price', 'Link'])


page = 1
while page <= 5:
    url = f'https://altersocks.com/products/page/{page}/'

    response = requests.get(url)
    content = response.text

    soup = BeautifulSoup(content, 'html.parser')

    section = soup.find('ul', class_='products clearfix products-5')
    # print(section)

    all_product = section.find_all('li')
    # print(all_product)

    for sock in all_product:

        #title
        prod_info = sock.find('h3', class_='product-title')
        title = prod_info.a.text.strip()

        #price
        price_info = sock.find('div', class_='fusion-price-rating')
        price = price_info.text.strip()

        #image
        image_addr = sock.img.attrs['src']

        #all information
        result = 'Name of sock: {} \nPrice: {} \nImmage link: {}\n'.format(title, price, image_addr)
        print(result)

        wr_obj.writerow([title, price, image_addr])
    page += 1
    time.sleep(random.randint(15, 20))







