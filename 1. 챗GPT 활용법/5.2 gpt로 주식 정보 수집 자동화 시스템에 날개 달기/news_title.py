import requests
from bs4 import BeautifulSoup
import csv

# 검색할 키워드와 페이지 수 설정
keyword = 'AAPL'
page_count = 10

# CSV 파일 생성 및 헤더 설정
with open('news_titles.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'emotion'])

# 검색 결과 페이지 순회하며 제목 추출
for page in range(1, page_count*10, 10):
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={page}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for news in soup.select('div.news_area'):
        title = news.select_one('a.news_tit').text

        # 추출한 제목 CSV 파일에 저장
        with open('news_titles.csv', mode='a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, ''])
            print(title)

