import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=vtizH9w0V7c&t=198s&ab_channel=%D0%A5%D0%B0%D1%83%D0%B4%D0%B8%D0%A5%D0%BE%E2%84%A2-%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%BE%D0%BC%D0%B8%D1%80%D0%B5IT%21'
r = requests.get(url)
rbs = BeautifulSoup(r.content, 'lxml')
print(rbs)