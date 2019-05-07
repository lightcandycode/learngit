import requests
from bs4 import BeautifulSoup
import turtle
content = requests.get('http://www.baidu.com').content
soup = BeautifulSoup(content, 'html.parser')
for div in soup.find_all('div', {'class': 'content'}):
    print(div.text.strip())
print(5+10)
print(7, 97)
print(5**2)
print(2**7)
