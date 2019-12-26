import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
html = requests.get(url).text
soup = BeautifulSoup(html)

# class명이 sh_blog_title인 모든 녀석
title =soup.find_all(class_='sh_blog_title')


for i in title:
    name = i.attrs['title']
    address = i.attrs['href']

    print(name, address)    
