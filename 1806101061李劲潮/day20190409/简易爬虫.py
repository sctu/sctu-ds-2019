#库的使用
import requests
from bs4 import BeautifulSoup

#确定待抓取URL
url = 'https://www.qiushibaike.com/text/'

#确定抓取数据
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

#处理解析抓回数据
soup = BeautifulSoup(html,features="lxml")
joke = soup.select('div.content')[0].get_text()

#将数据保存本地
with open('joke.txt','w',encoding='utf-8')as f:
    f.write(joke)