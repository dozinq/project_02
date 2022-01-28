import requests

# 1. URL
URL = 'https://api.agify.io?name=michael'

# 2. 요청
response = requests.get(URL).json()
print(response.get('age'))