import requests
from pprint import pprint


def recommendation(title):
    # 여기에 코드를 작성합니다.

    # 수집하고자 하는 정보가 담겨 있는 URL_search를 작성하였다.
    URL_search = 'https://api.themoviedb.org/3/search/movie'
    # 아래의 params_search 딕셔녀리를 통해 요청 변수를 기재해 주었습니다.
    params_search = {
    'api_key' : '', # (api_key 값은 마지막 시점에 모두 삭제하였습니다.)
    'language' : 'ko-KR',
    'region' : 'KR',
    'query' : title
    }
    # 요청 결과를 저장하였다.
    response_01 = requests.get(URL_search, params = params_search)
    # data_01 변수에 json형식으로 저장하였다.
    data_01 = response_01.json()
    # 'results'항목의 값(영화 정보들)을 data_lst_01에 담았다.
    data_lst_01 = data_01.get('results')
    
    # 반복문을 통해 인덱스가 하나하나 검토할 수 있도록 하였다.
    for index in data_lst_01:
        # 영화 정보들 중에서 각 'id'항목의 값을 movie_id에 담았다.
        movie_id = index.get('id')
        # UnboundLocalError가 발생하므로, if-else문을 for문 안에 삽입하여 해결한다.
        # if문은 검색이 안 될 경우 예외처리를 함으로 해결하였다.
        if len(str(movie_id)) == 0: 
            return None
        # else문으로 다음 해결 사항을 작성하였다.
        else:
            URL_recommendations = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
            params_recommendations = {
                'api_key' : '', # (api_key 값은 마지막 시점에 모두 삭제하였습니다.)
                'language' : 'ko-KR',
                'region' : 'KR'
            }
            # 요청 결과를 저장하였다.
            response_02 = requests.get(URL_recommendations, params = params_recommendations)
            # data_02 변수에 json형식으로 저장하였다.
            data_02 = response_02.json()
            # 'results'항목의 값(영화 정보들)을 data_lst_02에 담았다.
            data_lst_02 = data_02.get('results')
            # 마지막으로 반환할 리스트를 비어있는 상태로 만들어 놓았다.
            movie_recommendation_lst =[]
            # 반복문을 통해, 키 값이 'title'로 되어 있는 value값을 만들어 놓은 리스트에 누적시킨다.
            for index in data_lst_02:
                movie_recommendation_lst.append(index.get('title'))
            # 누적된 리스트를 반환하여, 결과값을 도출해 낸다.
            return movie_recommendation_lst

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
