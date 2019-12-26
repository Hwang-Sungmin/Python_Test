import requests
import parser
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='
#input으로 입력 받는 값
plusUrl = input('검색어를 입력하세요 : ')
url = baseUrl + plusUrl
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

# class명이 sh_blog_title인 모든 녀석
title =soup.find_all(class_='sh_blog_title')
for i in title:
    name = i.attrs['title']
    address = i.attrs['href']

    print(name, address)    
