import requests
from pprint import pprint


def ranking():
    # 여기에 코드를 작성합니다.

    # 수집하고자 하는 정보가 담겨 있는 URL을 작성하였다.
    URL = 'https://api.themoviedb.org/3/movie/popular'
    # 아래의 params 딕셔녀리를 통해 요청 변수를 기재해 주었습니다.
    params = {
    'api_key' : '', # (api_key 값은 마지막 시점에 모두 삭제하였습니다.)
    'language' : 'ko-KR',
    'region' : 'KR'
    }
    # 요청 결과를 저장하였다.
    response = requests.get(URL, params = params)
    # data 변수에 json형식으로 저장하였다.
    data = response.json()
    # 반환값을 저장할 빈 리스트를 만들어주었다.
    ans_lst = []
    # 'results'항목의 값(영화 정보들)을 data_lst에 담았다.
    data_lst = data.get('results')
    # data_lst를 대상으로 평점을 기준으로 높은 순서대로 정렬하였고, 이를 ranking에 담았다.
    ranking = sorted(data_lst, key = lambda i : i['vote_average'], reverse = True)
    # ranking 5위까지의 정보만 슬라이싱을 통해 ans_lst로 담아두었다.
    ans_lst = ranking[:5]
    # ans_lst를 반환하였다.
    return ans_lst

if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
