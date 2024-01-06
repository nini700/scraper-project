import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

url = 'https://www.dell.com/en-us/shop/dell-laptops/sr/laptops/xps?appliedRefinements=37868,37873,37869,37867,37865'
headers = {os.getenv('AGENT') : os.getenv('DATA')}

req = requests.get(url, headers = headers)
