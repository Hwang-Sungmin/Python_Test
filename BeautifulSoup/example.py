import requests
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusUrl = input('검색어를 입력 : ')
url = baseUrl + plusUrl
print(url)
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

title = soup.find_all(class_="sh_blog_title")

for i in title:
    name = i.attrs['title']

    print(name)