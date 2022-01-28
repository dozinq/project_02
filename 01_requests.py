import requests
from bs4 import BeautifulSoup

# 1-1. 주소
URL = 'https://finance.naver.com/sise/'
# 1-2. 요청
# https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
#response(200) : 성공적으로 가져왔다! cf. 404error : 내 잘못 / 500 : 서버 내부 에러
response = requests.get(URL)
# print(type(response)) #type : string

# 2.1 BeautifulSoup (text -> 다른 객체)
# Beautiful Soup is a Python library for pulling data out of HTML and XMl files.
# HTML 파일에 있는 데이터를 가져오기 위해서 활용
data = BeautifulSoup(response, 'html.pareser')
# print(type(data), type(response)) # <class 'bs4.BeautifulSoup'> <class 'str'>

# 2-2. 내가 원하는 정보를 가져온다 !
# 선택자(selector)
kospi = data.select_one('#KOSPI_now')
print(kospi.text)