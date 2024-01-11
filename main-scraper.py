import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pydantic import BaseModel, field_validator

load_dotenv()

class Laptop(BaseModel):
    model: str
    curr_price: float
    processor: str
    os: str
    graphics: str
    memory: str
    storage: str
    
    @field_validator('curr_price', mode = 'before')
    def price_valid(cls, value):
        if isinstance(value, str):
            fixed = value.replace(',', '')
            return float(fixed)
        elif isinstance(value, float):
            return value
        else:
            raise TypeError('Type must be a float (or a string)!')

def get_NextPage(url, soup):
    if params['page'] <= 15:
        params['page'] += 1
        return requests.get(url, headers = headers, params = params)
    else:
        return 

params = {'page' : 1}
url = 'https://www.dell.com/en-us/shop/dell-laptops/sr/laptops/xps?appliedRefinements=37868,37873,37869,37867,37865'
headers = {os.getenv('AGENT') : os.getenv('DATA')}
req = requests.get(url, params = params, headers = headers)
soup = BeautifulSoup(req.content, 'html.parser')
laptop_list = []

while True:
    soup = BeautifulSoup(req.content, 'html.parser')
    req = get_NextPage(url, soup)
    if not req:
        break
    laptops = soup.find_all('article', class_ = 'stack-system ps-stack')
    for laptop in laptops:
        data_html = laptop.find_all('span', class_ = 'ps-iconography-specs-label')
        data = [i.text.lstrip().rstrip() for i in data_html]
        name = laptop.find('h3', class_ = 'ps-title').text.split('\n')
        price = laptop.find('div', class_ = 'ps-dell-price ps-simplified').text.split('$')
        instance = Laptop(model = name[1], curr_price = price, processor = data[0], os = data[1], graphics = data[2], memory = data[3], storage = data[4])
        laptop_list.append(instance)


if __name__ == '__main__':
    for laptop in laptop_list:
        print(laptop.curr_price, end = '\n')
