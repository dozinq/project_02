# 0. import
import requests

# 1. URL 및 요청변수 설정
    # https://developers.themoviedb.org/3/movies/get-now-playing
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/now_playing'
params = {
    'api_key' : '-', #"private_information_hide"
    'region' : 'KR',
    'language' : 'ko'
}

# 2. 요청보낸 결과 저장
response = requests.get(BASE_URL + path, params = params)
print(response.status_code, response.url)
data = response.json()

print(type(data)) #dict
print(data.keys()) #dict_keys(['dates', 'page', 'results', 'total_pages', 'total_results'])
print(type(data.get('results'))) #list
print(data.get('results')[0]) #list 첫번째 구조
print(type(data.get('results')[0])) #dict
print(len(data.get('results'))) #20개

# 3. 조작하기
# print(response)