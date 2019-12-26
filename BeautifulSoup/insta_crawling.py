from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
# 사용하는 이유
# 자바 스크립트로 되어 있어서
import time

baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input('검색할 키워드를 입력 : ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(url)

insta = soup.select('.v1Nh3')

print(insta)

driver.close()