
import os
import requests
import zipfile

# API 정보
client_id = "IrSIGyvKyVU43e4Xg47r"
client_secret = "wr05UNhgtc"

# 검색어 설정
query = "리시안셔스"

# API 요청 URL
url = "https://openapi.naver.com/v1/search/image?query=" + query + "&display=50&sort=sim"

# API 요청 헤더 설정
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}

# API 요청 보내기
response = requests.get(url, headers=headers)

# 검색 결과에서 이미지 URL 추출하기
items = response.json()['items']
image_urls = [item['link'] for item in items]

# 이미지 다운로드하기
if not os.path.exists('images'):
    os.makedirs('images')
for i, url in enumerate(image_urls):
    response = requests.get(url)
    with open('images/'+str(i)+'.jpg', 'wb') as f:
        f.write(response.content)

# 이미지 압축하기
with zipfile.ZipFile('images.zip', 'w') as zip:
    for foldername, subfolders, filenames in os.walk('images'):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            zip.write(filepath, arcname=filename)

print("다운로드 완료")
