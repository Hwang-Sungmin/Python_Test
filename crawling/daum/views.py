from django.shortcuts import render

import urllib.request 
from bs4 import BeautifulSoup
import requests

# Create your views here.


def test(request):
    
    url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # class명이 sh_blog_title인 모든 녀석
    title =soup.find_all(class_='sh_blog_title')

    for i in title:
        name = i.attrs['title']
        address = i.attrs['href']
       
        context = {
            'name' : name,
            'address' : address,
            
        }
    print(len(title))
    return render(request, 'test.html', context )

def mbam(request):
        
        
    return render(request, 'mbam.html')