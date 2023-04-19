import requests
import csv
from bs4 import BeautifulSoup

# 카테고리 ID에 대한 정보
categories = {
    "ALL": "전체",
    "50000000": "패션의류",
    "50000001": "패션잡화",
    "50000002": "화장품/미용",
    "50000003": "디지털/가전",
    "50000004": "가구/인테리어",
    "50000005": "출산/육아",
    "50000006": "식품",
    "50000007": "스포츠/레저",
    "50000008": "생활/건강",
    "50000009": "여행/문화"
}

# 각 카테고리에 대한 URL
urls = {
    cat: f"https://search.shopping.naver.com/best/category/keyword?categoryCategoryId={cat}&categoryDemo=A00&categoryRootCategoryId={cat}&chartRank=1&period=P1D"
    for cat in categories
}

with open('result.csv', mode='w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Rank', 'Keyword'])

    for cat, url in urls.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.select('.chartList_btn_keyword__Cqc0z')

        for i, item in enumerate(items):
            writer.writerow([categories[cat], i+1, item.text.strip()])


