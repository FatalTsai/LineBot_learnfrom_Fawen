import re
import requests
from bs4 import BeautifulSoup

class PTT():
    def PTT_Crawler():
        title = ""
        # 下載 Dcard 標題
        r = requests.get("https://www.ptt.cc/bbs/SENIORHIGH/index.html")

        html_str = r.text
        # 以 BeautifulSoup 解析 HTML 程式碼
        soup = BeautifulSoup(html_str, 'html.parser')
        play_selector = '.title a'
        for i in soup.select(play_selector):
            title += i.text

        return title