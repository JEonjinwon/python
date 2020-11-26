import requests
import json

url = "https://dapi.kakao.com/v2/search/web"

queryString = {'query' : '아이유'}
header = {'Authorization': 'KakaoAK b825c4ac69c3dc7595733eab474d07aa'}

response = requests.get(url, headers=header, params=queryString)
tokens = response.json()

print(response)
print(tokens)




