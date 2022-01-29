import requests
from pprint import pprint


def credits(title):
    # 여기에 코드를 작성합니다.

    # 결과값으로 반환하게 될 딕셔너리를 구성할 리스트들을 미리 선언해 놓았다.
    cast_name_lst = []
    crew_name_lst = []
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
            URL_credits = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
            params_credits = {
                'api_key' : '', # (api_key 값은 마지막 시점에 모두 삭제하였습니다.)
                'language' : 'ko-KR',
                'region' : 'KR'
            }
            # 요청 결과를 저장하였다.
            response_02 = requests.get(URL_credits, params = params_credits)
            # data_02 변수에 json형식으로 저장하였다.
            data_02 = response_02.json()
            #cast,crew list를 분리하여 cast_lst, crew_lst에 해당하는 값을 넣을 수 있게 하였다.
            cast_lst = data_02.get('cast')
            crew_lst = data_02.get('crew')
            #cast_name을 반복문을 통해 얻을 수 있게끔 하였고, cast_name_lst에 저장할 수 있게 하였다.
            for cast in cast_lst:
                cast_name_lst.append(cast.get('original_name'))
            #crew_name을 반복문을 통해 얻을 수 있게끔 하였고, crew_name_lst에 저장할 수 있게 하였다.
            for crew in crew_lst:
                # 조건문을 통해, 중복되는 값을 넣지 않았다.
                if crew_name_lst.count(crew.get('original_name')) == 0:
                    crew_name_lst.append(crew.get('original_name'))
                else:
                    continue
            # 리스트값으로 value값을 구성하여 해당 key에 맞게 딕셔너리를 구성하여 반환한다.
            return {'cast': cast_name_lst, 'crew' : crew_name_lst}


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
