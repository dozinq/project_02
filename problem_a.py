import requests


def popular_count(): 
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
    # print(response)
    # print(data.get('results')) # success!
    # print(type(data.get('results'))) # list
    # results 리스트의 길이를 반환함으로써, 영화목록의 개수를 출력하였습니다.
    return len(data.get('results'))

if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
