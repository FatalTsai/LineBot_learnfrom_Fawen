import re
import requests
from bs4 import BeautifulSoup

# 下載 Dcard 標題
r = requests.get("https://www.dcard.tw/f")

html_str = r.text
# 以 BeautifulSoup 解析 HTML 程式碼
soup = BeautifulSoup(html_str, 'html.parser')
play_selector = 'span'
for i in soup.select(play_selector):
    print(i.text)