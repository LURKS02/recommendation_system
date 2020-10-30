import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def data_recommend(movieName):
    data = pd.read_csv('./movies_metadata.csv')

    data = data[['id', 'genres', 'popularity', 'imdb_id', 'overview', 'title', 'tagline', 'vote_average', 'vote_count']]

    """ 백분위수 구하기
    quantile : 해당 백분위에 해당하는 값 (vote_count)
    loc : 행단위 데이터 읽기 (인덱스 값 기준)
    """
    # vote 수가 적은 경우 정확한 평점을 표시하기 어렵기 때문에
    # rating의 공정성을 높이기 위해
    # imdb에서 제안하는 가중치가 적용된 rating을 계산해야함
    m = data['vote_count'].quantile(0.9)
    data = data.loc[data['vote_count'] >= m]
    data = data.reset_index()[['id', 'genres', 'popularity', 'imdb_id', 'overview', 'title', 'tagline', 'vote_average', 'vote_count']]

    # 가중치가 젹용된 rating을 계산한 weighted score 값을 계산,
    # dataset에 새로운 필드로 추가함.
    C = data['vote_average'].mean()
    def weighted_rating(x, m=m, C=C) :
        v = x['vote_count']
        R = x['vote_average']
        return (v / (v+m) * R) + (m / (m + v) * C)
    data['score'] = data.apply(weighted_rating, axis = 1)

    # 데이터 전처리 과정
    # 배열 형식의 문자열을 list로 쪼개고 id를 제외한 name값들만 추출
    data['genres'] = data['genres'].apply(literal_eval)
    data['genres'] = data['genres'].apply(lambda x : [d['name'] for d in x]).apply(lambda x : " ".join(x))

    """CountVectorizer : 문서에서 단어의 빈도수를 계산하여 문서 단어 행렬을 생성
    문서를 토큰 리스트로 변환
    각 문서에서 토근의 출현 빈도를 셈
    각 문서를 BOW인코딩 벡터로 변환
    """

    """
    <Content based filtering>
    비슷한 콘텐츠를 사용자에게 추천
    """
    # 장르를 이용한 추천
    # 문자열로 구성된 장르를 숫자로 바꾸어 벡터화시켜야함
    # ngram_range(min, max) : 단어장 생성에 사용할 토큰의 크기
    count_vector = CountVectorizer(ngram_range = (1, 3))
    c_vector_genres = count_vector.fit_transform(data['genres'])

    # cosine similarity
    # 코사인 유사도 + vote_count가 높은 것 기반으로 추천
    # 각 영화의 유사도를 측정하여 비슷한 장르의 영화를 추천받을 수 있음.
    genre_c_sim = cosine_similarity(c_vector_genres, c_vector_genres).argsort()[:, ::-1] #내림차순

    def get_recommend_movie_list(df, movie_title, top=30):
        target_movie_index = df[df['title'] == movie_title].index.values
        sim_index = genre_c_sim[target_movie_index, :top].reshape(-1)
        sim_index = sim_index[sim_index != target_movie_index]
        result = df.iloc[sim_index].sort_values('score', ascending = False)[:10] #역순정렬
        return result

    return(get_recommend_movie_list(data, movie_title = movieName))

# 입력된 영화 제목에 해당하는 추천 리스트를 받아서 리턴
def data_recommend_title(movieName):
    movieTitleList = []
    data = data_recommend(movieName)
    for i in range(10) :
        movieTitleList.append(data.iloc[i]['title'])
    return movieTitleList

def movie_info(recommend_title, base_title):
    data = data_recommend(base_title)
    return data[data['title'] == recommend_title]
