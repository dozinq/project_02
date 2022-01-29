# 📌 My Second Project 📋

---

##### - Outline : 2022년 1월 28일, 두번째 프로젝트를 수행하였다. 지난 프로젝트에서 더 확장하여 이번에는 주어지지 않은 정보를 직접 요청(*requests*)하여 얻을 수 있었고, 그 정보를 이용하여 원하는 정보로 바꾸어내는 과정이 담겨있다. 이번 프로젝트를 진행하면서 내가 느꼈던 점을 중심으로 소개해 보고자 한다.

---

<br/>

# **< Title : " Python을 활용한 데이터 수집 Ⅱ *"* >**

*(This project was carried out in **Python 3.9.9 environment.**)*

- *요구사항 : 커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 영화 데이터를 수집하는 과정입니다. 아래 기술된 사항은 필수적으로 구현해야 하는 내용입니다. 완성된 기능들은 향후 커뮤니티 서비스에서 활용할 수 있습니다.*

<br/>

#### - case #1. 제공되는 영화 데이터의 주요내용 수집

*: 인기 영화의 개수를 출력한다.*

```python
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
```

```python
# 결과 :
20
```

> 처음 requests 클래스를 가져온 것에 대한 활용 방법에 대해서 많이 헤맸었다. 그러다가 어떻게 하는 방법인지 교육을 통해 충분히 깨닫게 되었었고, 그것을 토대로 작성해 보았다. 문제의 해결은 원하는 정보를 도출하는 것이었기에, 그동안에 배웠던 지식으로 충분히 해결할 수 있었음에 보람을 많이 느꼈다.

<br/>


#### - case #2. 특정 조건에 맞는 인기 영화 조회Ⅰ

*: popular를 기준으로 가져온 영화 목록 중 평점이 8 이상인 영화들의 목록을 출력한다.*

```python
import requests
from pprint import pprint


def vote_average_movies():
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
    # 반복문을 통해 인덱스가 하나하나 검토할 수 있도록 하였다.
    for index in data_lst:
        # 인덱스가 얻은 평점을 8이상인 값들만 추출할 수 있도록 하였다.
        if index.get('vote_average') >= 8:
            ans_lst.append(index)
    # 담겨진 리스트를 반환하였다.
    return ans_lst
```

```python
# 결과 :
[{'adult': False,
  'backdrop_path': '/iQFcwSGbZXMkeyKrxbPnwnRo5fl.jpg',
  'genre_ids': [28, 12, 878],
  'id': 634649,
  'original_language': 'en',
  'original_title': 'Spider-Man: No Way Home',
  'overview': '정체가 탄로난 스파이더맨 피터 파커가 시간을 되돌리기 위해 닥터 스트레인지의 도움을 받던 중 뜻하지 않게 '
              '멀티버스가 열리게 되고, 이를 통해 자신의 숙적 닥터 옥토퍼스가 나타나며 사상 최악의 위기를 맞게 되는데...',
  'popularity': 18473.631,
  'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
  'release_date': '2021-12-15',
  'title': '스파이더맨: 노 웨이 홈',
  'video': False,
  'vote_average': 8.5,
  'vote_count': 6194},
 {'adult': False,
  'backdrop_path': '/tutaKitJJIaqZPyMz7rxrhb4Yxm.jpg',
  'genre_ids': [35, 16, 10751, 10402],
  'id': 438695,
  'original_language': 'en',
  'original_title': 'Sing 2',
  'overview': '대국민 오디션 이후 각자의 자리에서 꿈을 이루고 있는 버스터 문(매튜 맥커너히)과 크루들에게 레드 쇼어 시티에서 '
              '전 세계가 주목하는 사상 최고의 쇼가 펼쳐진다는 소식이 들려오고 버스터 문과 크루들은 도전에 나선다. 그러나 '
              '최고의 스테이지에 서기 위한 경쟁은 이전과는 비교도 할 수 없을 만큼 치열하고, 버스터 문은 완벽한 라이브를 위해 '
              '종적을 감춘 레전드 뮤지션 클레이(보노)를 캐스팅하겠다는 파격 선언을 하는데!',
  'popularity': 3699.266,
  'poster_path': '/xe8dVB2QiCxLWFV77V4dpZcOvYB.jpg',
  'release_date': '2022-01-05',
  'title': '씽2게더',
  'video': False,
  'vote_average': 8.3,
  'vote_count': 1388},
 {'adult': False,
  'backdrop_path': '/xPpXYnCWfjkt3zzE0dpCNME1pXF.jpg',
  'genre_ids': [16, 28, 12, 14],
  'id': 635302,
  'original_language': 'ja',
  'original_title': '劇場版「鬼滅の刃」無限列車編',
  'overview': '혈귀로 변해버린 여동생 네즈코를 인간으로 되돌릴 단서를 찾아 비밀조직 귀살대에 들어간 탄지로. 젠이츠, 이노스케와 '
              '새로운 임무 수행을 위해 무한열차에 탑승 후 귀살대 최강 검사 염주 렌고쿠와 합류한다. 달리는 무한열차에서 '
              '승객들이 하나 둘 흔적 없이 사라지자 숨어있는 식인 혈귀의 존재를 직감하는 렌고쿠. 귀살대 탄지로 일행과 최강 '
              '검사 염주 렌고쿠는 어둠 속을 달리는 무한열차에서 모두의 목숨을 구하기 위해 예측불가능한 능력을 가진 혈귀와 '
              '목숨을 건 혈전을 시작하는데...',
  'popularity': 1179.343,
  'poster_path': '/m2FNRngyJMyxLatBMJR8pbeG2v.jpg',
  'release_date': '2021-01-27',
  'title': '귀멸의 칼날 극장판 무한열차편',
  'video': False,
  'vote_average': 8.4,
  'vote_count': 2073},
 {'adult': False,
  'backdrop_path': '/oE6bhqqVFyIECtBzqIuvh6JdaB5.jpg',
  'genre_ids': [878, 18, 12],
  'id': 522402,
  'original_language': 'en',
  'original_title': 'Finch',
  'overview': '감마 플레어가 오존층을 파괴하고 전자기 펄스가 모든 전기를 흡수하면서 지상은 황폐화되고 대부분의 인류는 사망한 '
              '가까운 미래. 살아남은 소수의 인류는 자외선과 고온을 피해 밤에 활동하고, 먹을 것과 생필품을 구하기 위해 잔인한 '
              '본성을 드러낸다. 살아남은 TAE 테크놀로지의 과학자 핀치 와인버그(톰 행크스)는 사랑하는 개 굿이어와 함께 '
              '미주리의 폐허 속에서 먹을 것과 생필품을 찾는다. 병들어 죽음을 앞두고 있는 핀치는 굿이어를 돌봐줄 수 있는 '
              '인공지능 로봇을 만들고 데이터를 업로드한다. 얼마 후 40일간 지속되는 거대한 폭풍이 핀치의 은신처로 다가오자, '
              '핀치는 안드로이드와 굿이어, 그리고 운반 로봇 듀이와 함께 트럭을 타고 급히 서쪽 샌프란시스코로 향하는데...',
  'popularity': 644.739,
  'poster_path': '/jKuDyqx7jrjiR9cDzB5pxzhJAdv.jpg',
  'release_date': '2021-11-05',
  'title': '핀치',
  'video': False,
  'vote_average': 8.1,
  'vote_count': 1864},
 {'adult': False,
  'backdrop_path': '/sdL37sfUBth7mdkAolI83bXAl7L.jpg',
  'genre_ids': [16, 878, 10751, 35],
  'id': 482321,
  'original_language': 'en',
  'original_title': "Ron's Gone Wrong",
  'overview': '최첨단 소셜 AI 로봇 비봇이 모든 아이들의 친구가 되는 세상. 비봇을 갖는 것이 유일한 소원인 소심한 소년 '
              '바니에게도 드디어 론이라는 비봇이 생겼다. 그러나 첨단 디지털 기능과 소셜 미디어로 연결된 다른 비봇들과는 달리, '
              '네트워크 접속이 불가능한 고장난 론. 자유분방하고 엉뚱한 론으로 인해 벌어지는 엉망진창, 스릴 넘치는 모험을 '
              '함께하며 바니는 진실한 우정이 무엇인지 점점 깨닫게 되는데..',
  'popularity': 592.877,
  'poster_path': '/ljYdrF1faaWbzcrZuQ6BTqfVHcS.jpg',
  'release_date': '2021-10-27',
  'title': '고장난 론',
  'video': False,
  'vote_average': 8.2,
  'vote_count': 767}]
```

> 첫 번째 케이스와 유사하게 접근하면 되었고, 그것에 더하여 조건문을 필수적으로 작성해야 했다. 무턱대고 작성하기에 앞서 내가 무엇을 해야 하는지 정확하게 깨닫고자 노력하였고, 생각을 그대로 작성해서 보다 쉽게 해결할 수 있었던 케이스였다. 그동안 흔히 보았던 기준 이상의 평점으로 보여주는 것도 결국은 모두 프로그래밍이라는 사실이 당연했음에도 많이 놀랐다.

<br/>


#### - case #3. 특정 조건에 맞는 인기 영화 조회Ⅱ

*: 영화목록을 평점순으로 출력하는 함수를 완성한다. 해당 기능은 향후 커뮤니티 서비스에서 기본으로 제공되는 영화 정보로 사용된다고 한다.*

```python
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
```

```python
# 결과 :
[{'adult': False,
  'backdrop_path': '/iQFcwSGbZXMkeyKrxbPnwnRo5fl.jpg',
  'genre_ids': [28, 12, 878],
  'id': 634649,
  'original_language': 'en',
  'original_title': 'Spider-Man: No Way Home',
  'overview': '정체가 탄로난 스파이더맨 피터 파커가 시간을 되돌리기 위해 닥터 스트레인지의 도움을 받던 중 뜻하지 않게 '
              '멀티버스가 열리게 되고, 이를 통해 자신의 숙적 닥터 옥토퍼스가 나타나며 사상 최악의 위기를 맞게 되는데...',
  'popularity': 18473.631,
  'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
  'release_date': '2021-12-15',
  'title': '스파이더맨: 노 웨이 홈',
  'video': False,
  'vote_average': 8.5,
  'vote_count': 6194},
 {'adult': False,
  'backdrop_path': '/xPpXYnCWfjkt3zzE0dpCNME1pXF.jpg',
  'genre_ids': [16, 28, 12, 14],
  'id': 635302,
  'original_language': 'ja',
  'original_title': '劇場版「鬼滅の刃」無限列車編',
  'overview': '혈귀로 변해버린 여동생 네즈코를 인간으로 되돌릴 단서를 찾아 비밀조직 귀살대에 들어간 탄지로. 젠이츠, 이노스케와 '
              '새로운 임무 수행을 위해 무한열차에 탑승 후 귀살대 최강 검사 염주 렌고쿠와 합류한다. 달리는 무한열차에서 '
              '승객들이 하나 둘 흔적 없이 사라지자 숨어있는 식인 혈귀의 존재를 직감하는 렌고쿠. 귀살대 탄지로 일행과 최강 '
              '검사 염주 렌고쿠는 어둠 속을 달리는 무한열차에서 모두의 목숨을 구하기 위해 예측불가능한 능력을 가진 혈귀와 '
              '목숨을 건 혈전을 시작하는데...',
  'popularity': 1179.343,
  'poster_path': '/m2FNRngyJMyxLatBMJR8pbeG2v.jpg',
  'release_date': '2021-01-27',
  'title': '귀멸의 칼날 극장판 무한열차편',
  'video': False,
  'vote_average': 8.4,
  'vote_count': 2073},
 {'adult': False,
  'backdrop_path': '/tutaKitJJIaqZPyMz7rxrhb4Yxm.jpg',
  'genre_ids': [35, 16, 10751, 10402],
  'id': 438695,
  'original_language': 'en',
  'original_title': 'Sing 2',
  'overview': '대국민 오디션 이후 각자의 자리에서 꿈을 이루고 있는 버스터 문(매튜 맥커너히)과 크루들에게 레드 쇼어 시티에서 '
              '전 세계가 주목하는 사상 최고의 쇼가 펼쳐진다는 소식이 들려오고 버스터 문과 크루들은 도전에 나선다. 그러나 '
              '최고의 스테이지에 서기 위한 경쟁은 이전과는 비교도 할 수 없을 만큼 치열하고, 버스터 문은 완벽한 라이브를 위해 '
              '종적을 감춘 레전드 뮤지션 클레이(보노)를 캐스팅하겠다는 파격 선언을 하는데!',
  'popularity': 3699.266,
  'poster_path': '/xe8dVB2QiCxLWFV77V4dpZcOvYB.jpg',
  'release_date': '2022-01-05',
  'title': '씽2게더',
  'video': False,
  'vote_average': 8.3,
  'vote_count': 1388},
 {'adult': False,
  'backdrop_path': '/sdL37sfUBth7mdkAolI83bXAl7L.jpg',
  'genre_ids': [16, 878, 10751, 35],
  'id': 482321,
  'original_language': 'en',
  'original_title': "Ron's Gone Wrong",
  'overview': '최첨단 소셜 AI 로봇 비봇이 모든 아이들의 친구가 되는 세상. 비봇을 갖는 것이 유일한 소원인 소심한 소년 '
              '바니에게도 드디어 론이라는 비봇이 생겼다. 그러나 첨단 디지털 기능과 소셜 미디어로 연결된 다른 비봇들과는 달리, '
              '네트워크 접속이 불가능한 고장난 론. 자유분방하고 엉뚱한 론으로 인해 벌어지는 엉망진창, 스릴 넘치는 모험을 '
              '함께하며 바니는 진실한 우정이 무엇인지 점점 깨닫게 되는데..',
  'popularity': 592.877,
  'poster_path': '/ljYdrF1faaWbzcrZuQ6BTqfVHcS.jpg',
  'release_date': '2021-10-27',
  'title': '고장난 론',
  'video': False,
  'vote_average': 8.2,
  'vote_count': 767},
 {'adult': False,
  'backdrop_path': '/oE6bhqqVFyIECtBzqIuvh6JdaB5.jpg',
  'genre_ids': [878, 18, 12],
  'id': 522402,
  'original_language': 'en',
  'original_title': 'Finch',
  'overview': '감마 플레어가 오존층을 파괴하고 전자기 펄스가 모든 전기를 흡수하면서 지상은 황폐화되고 대부분의 인류는 사망한 '
              '가까운 미래. 살아남은 소수의 인류는 자외선과 고온을 피해 밤에 활동하고, 먹을 것과 생필품을 구하기 위해 잔인한 '
              '본성을 드러낸다. 살아남은 TAE 테크놀로지의 과학자 핀치 와인버그(톰 행크스)는 사랑하는 개 굿이어와 함께 '
              '미주리의 폐허 속에서 먹을 것과 생필품을 찾는다. 병들어 죽음을 앞두고 있는 핀치는 굿이어를 돌봐줄 수 있는 '
              '인공지능 로봇을 만들고 데이터를 업로드한다. 얼마 후 40일간 지속되는 거대한 폭풍이 핀치의 은신처로 다가오자, '
              '핀치는 안드로이드와 굿이어, 그리고 운반 로봇 듀이와 함께 트럭을 타고 급히 서쪽 샌프란시스코로 향하는데...',
  'popularity': 644.739,
  'poster_path': '/jKuDyqx7jrjiR9cDzB5pxzhJAdv.jpg',
  'release_date': '2021-11-05',
  'title': '핀치',
  'video': False,
  'vote_average': 8.1,
  'vote_count': 1864}]
```

> 두 번째 케이스와 매우 유사하였던 세 번째 케이스여서 비교적 쉽게 느껴졌고 해결하는 것에도 손이 가지 않았었다. 평점순으로 나열하고 그 중 다섯개의 결과만 나타내 주는 것을 이렇게 스스로도 구현해 낼 수 있다는 것이 많이 신기했다.

<br/>

#### - case #4. 특정 영화 추천 영화 조회

*: 제공된 영화 제목을 기준으로 추천영화 목록을 출력한다. 제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록을 구성하고, 추천 영화가 없을 경우 []을 반환하고, 영화 id검색에 실패할 경우에는 None을 반환한다.*

```python
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
```

```python
# 결과 :
['조커',
 '조조 래빗',
 '1917',
 '원스 어폰 어 타임 인… 할리우드',  
 '결혼 이야기',
 '나이브스 아웃',
 '아이리시맨',
 '포드 V 페라리',
 '작은 아씨들',
 '라이트하우스',
 '미드소마',
 '언컷 젬스',
 '더 플랫폼',
 '스타워즈: 라이즈 오브 스카이워커',
 '두 교황',
 '애드 아스트라',
 '그린 북',
 '살인의 추억',
 '센과 치히로의 행방불명',
 '버즈 오브 프레이: 할리 퀸의 황홀한 해방',
 '토이 스토리 4']
[]
None
```

> 네 번째 케이스에서는 많이 애를 먹었었다. 일단, 두 번에 걸쳐서 requests를 하여야 했고, 처음 요청의 결과를 응용하여 결국 해결하기까지, 많이 복합적인 사고가 필요했다. 순서를 도입하되 근거가 있어야 했다. 그래서 생각하는 시간이 많이 필요하였고, 충분한 시간동안 생각하고 작성하여 해결할 수 있었다.

<br/>


#### - case #5. 배우, 감독 리스트 출력

*: 영화에 출연한 배우들과 감독의 정보가 저장된 딕셔너리를 출력한다.*

```python
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
```

```python
# 결과 :
{'cast': ['Song Kang-ho',
          'Lee Sun-kyun',
          'Cho Yeo-jeong',
          'Choi Woo-shik',
          'Park So-dam',
          'Lee Jung-eun',
          'Jang Hye-jin',
          'Park Myung-hoon',
          'Jung Ji-so',
          'Jung Hyeon-jun',
          'Park Keun-rok',
          'Jung Yi-seo',
          'Cho Jae-myung',
          'Jeong Ik-han',
          'Kim Gyu-baek',
          'Ahn Seong-bong',
          'Yoon Young-woo',
          'Park Jae-wook',
          'Lee Dong-yong',
          'Jeon Eun-mi',
          'Kim Geon',
          'Lee Joo-hyung',
          'Lee Ji-hye',
          'Kim Bo-ryeong',
          'Park Hye-sook',
          'Baek Seung-hwan',
          'Riccardo Ferraresso',
          'Ko Kwan-jae',
          'Lee Si-hoon',
          'Seo Bok-hyeon',
          'Shim Soo-mi',
          'Yoon Hye-ree',
          'Andreas Fronk',
          'Anna Elisabeth Rihlmann',
          'Rosie Peralta',
          'Shin Seung-min',
          'Park Seo-jun',
          'Kwak Sin-ae',
          'Kim Yeong-jo',
          'Choi Jeong-hyun'],
 'crew': ['Bong Joon-ho',
          'Miky Lee',
          'Hong Kyung-pyo',
          'Lee Ji-yeon',
          'Choi Woo-shik',
          'Lee Jae-hyeok',
          'Choi Se-yeon',
          'Moon Yang-kwon',
          'Park Jeong-ja',
          'Kim Dae-hwan',
          'James Wright',
          'Eun Hui-su',
          'Yang Jin-mo',
          'Lee Ha-jun',
          'Cho Won-woo',
          'Park Hyun-cheol',
          'Han Mi-yeon',
          'Choi Tae-young',
          'Jin Her',
          'Kwak Tae-yong',
          'Lee Hee-eun',
          'Gang Hye-yeong',
          'Oh Se-Yeong',
          'Park Hyo-shin',
          'Jung Jae-il',
          'Kevin Kang',
          'Jang Young-hwan',
          'Kwak Sin-ae',
          'Sohn Suk-hee',
          'Kim Seo-young',
          'Kim Chang-ho',
          'Lee Chung-gyu',
          'Kim Ji-su',
          'Lee Hyang-Hee',
          'Hong Jeong-ho',
          'Heo Min-heoi',
          'Han Jin-won',
          'Kang Dong-yul',
          'Kim Seong-sik',
          'Oh You-jin',
          'Yoo Sang-seob',
          'Jeong Do-an',
          'Park Min-cheol',
          'Jeon Jae-wook',
          'Lim Myeong-gyun',
          'Kim Kyeong-taek',
          'Mo So-ra',
          'Hwang Hyo-gyun',
          'Park Kyoung-soo',
          'Lee Seon-yeong',
          'Kim Bo-ra',
          'Sung Oh Moon',
          'Son Won-rak',
          'Lee Joo-hyun',
          'Bae Kyung-hye',
          'Kim Sang-soo',
          'Nam Sung-ho',
          'Lee Jung-hoon',
          'Yoon Young-woo',
          'Samuel King',
          'Kim Byung-in',
          'Shin i Na',
          'Park Sung-gyun',
          'Peter Ahn',
          'Cha Dong-ho',
          'Choi Seung-goo',
          'Ha Jae-gu',
          'Seo Young Heo',
          'Jeong Ho Hong',
          'Huh Soo-jung',
          'Hwang Eun-bi',
          'Cheong Hyun-jun',
          'Andras Ikladi',
          'Jay Seung Jaegal',
          'Jang Hansaem',
          'Jang Hyo-sun',
          'Jang Mi-jin',
          'Jo Eun-byul',
          'Jung Seock-hee',
          'Jung Da-som',
          'Jung Ji-hyung',
          'Jung Sung-jin',
          'Jung Yeo-jin',
          'Jung Yeon-tae',
          'Kang Dong-hyuk',
          'Kang Jong-ik',
          'Kang Seong-pil',
          'Kang Won-chul',
          'Kim Bok-yung',
          'Chan-Jin Chris Kim',
          'Kim Eun-ji',
          'Kim Hyeong-gi',
          'Kim Jae-hwan',
          'Kim Sang-hun',
          'Kim Tae-hoon',
          'Kim Tae-hyung',
          'Kim Tae-seob',
          'Kim Woo-ju',
          'Ko Hee-kyung',
          'Kong Miseon',
          'Kwon Yong-ho',
          'Lee Dong Kyu',
          'Lee Eun-seon',
          'Hanhee Hailey Lee',
          'Lee Jae-wook',
          'Lee Kyoung-min',
          'Lee Min-ho',
          'Lee Sang-yeol',
          'Lee Sin-woo',
          'Lee Song-hee',
          'Lee Young-young',
          'Liang Jun-ling',
          'Lim Tae-woo',
          'Jeong Min-hyuk',
          'Oh Yu-min',
          'Park Hwon',
          'Park Hye-ri',
          'Park Ji-hyeon',
          'Park Sung-hyeok',
          'Ryu Ga-hee',
          'Seok Jong-yeon',
          'Lee Seung-yeon',
          'Shin Jeong-ho',
          'Son Young-nam',
          'Kim So-yoon',
          'Ahnwoo Yang',
          'Yeom Do-seon',
          'You Hyeon-jeong',
          'Youn Min-seok',
          'Yu Mi-hwa',
          'Yun Hee',
          'Yun Junshik-Raul',
          'Byun Sang-jin',
          'Sung Min Cha',
          'Cho Hye-lin',
          'Sang Won Cho',
          'Lee Su-jin',
          'Kim Hee-jae',
          'Shin Soo-bin',
          'Yoon Hye-jeong',
          'Yoon Na-yeon',
          'Norbert Elek',
          'Lee Ji-hye',
          'Bálint Sapszon',
          'Woo Geum-ho',
          'Noh Seung-goog',
          'Yoo Mi-jin',
          'Kim Tae-yeon',
          'Yang Hyeon-seok']}
```

> 네 번째 케이스를 응용하면 마지막 케이스의 문제도 쉽게 풀 수 있었다. 형식의 차이일 뿐이지 순서는 같았기 때문이다. 결과 값은 네 번째의 결과와 아예 다르지만, 결국 내가 원하는 것을 도출하기 까지 과정은 같았다. 그래서 비교적 쉽게 마무리할 수 있었던 것 같다.

<br/>


## ✏After finishing..

>   　　아주 자그마한 문제푸는 프로젝트에 지나지 않지만, 그래도 소중한 경험이라고 생각하고 누군가 원하는 결과를 도출해 낼 수 있다는 것에 큰 만족과 보람을 가질 수 있게 되었다. 또한, 내가 먼저 해결하였을 때 모르는 동기생에게 도움을 줄 수 있다는 것에 스스로도 많이 놀라기도 했었던 과제였다. 이번 과제를 통해 정보를 어떻게 해야 더 잘 응용할 수 있는지 알게 되었고, 내가 지금까지 배웠던 것이 정말 적은 양이기도 한데, 이것을 가지고도 해결할 수 있다는 게 큰 감동으로 나에게 다가와주기도 하였다. 앞으로도 프로젝트 뿐만 아니라 매우 많은 것을 배우고 그것을 활용해야 할 텐데, 나 자신을 믿어보기로 하였다. 그렇게 생각할 수 있게 해준 이 시간에 그저 감사할 뿐이다.