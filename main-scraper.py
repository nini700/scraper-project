import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

class Laptop:
    def __init__(self, curr_price, processor, os, graphics, memory, storage, display):
        self.__curr_price = curr_price
        self.__processor = processor
        self.__os = os
        self.__graphics = graphics
        self.__memory = memory
        self.__storage = display
    def get_Data(self):
        return [self.__curr_price, self.__processor, self.__os, self.__graphics, self.__memory, self.__storage]

url = 'https://www.dell.com/en-us/shop/dell-laptops/sr/laptops/xps?appliedRefinements=37868,37873,37869,37867,37865'
headers = {os.getenv('AGENT') : os.getenv('DATA')}
req = requests.get(url, headers = headers)
soup = BeautifulSoup(req.content, 'html.parser')
first = soup.find_all('article', class_ = 'stack-system ps-stack')
