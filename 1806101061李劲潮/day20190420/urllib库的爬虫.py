import urllib.request

response = urllib.request.urlopen('https://movie.douban.com/',None,2)

html = response.read().decode('utf8')

f = open('html.txt','w',encoding='utf8')

f.write(html)

f.close()

