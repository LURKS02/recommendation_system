import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('./movies_metadata.csv')

data = data[['id', 'genres', 'popularity', 'title', 'vote_average', 'vote_count']]
print(data)
print(data.head(2))
print(data.shape)

""" 백분위수 구하기
quantile : 해당 백분위에 해당하는 값 (vote_count)
loc : 행단위 데이터 읽기 (인덱스 값 기준)
"""
m = data['vote_count'].quantile(0.9)
print("vote_count = " + str(m))
data = data.loc[data['vote_count'] >= m]
#index번호 초기화
data = data.reset_index()[['id', 'genres', 'popularity', 'title', 'vote_average', 'vote_count']]
print("data = " + str(data.shape))
print(data.head())

#평균 구하기
C = data['vote_average'].mean()
print(C)

def weighted_rating(x, m=m, C=C) :
    v = x['vote_count']
    R = x['vote_average']
    return (v / (v+m) * R) + (m / (m + v) * C)

#score 필드 추가
data['score'] = data.apply(weighted_rating, axis = 1)
print(data.head())
print(data.shape)

#배열 형식의 문자열을 list로 쪼개기
data['genres'] = data['genres'].apply(literal_eval)
print(data[['genres']].head(2))

"""
apply() : 행/열/전체 셀에 원하는 연산 지원
lambda( arguments : expression ) : 
"""
data['genres'] = data['genres'].apply(lambda x : [d['name'] for d in x]).apply(lambda x : " ".join(x))
print(data.head(2))

#아랫줄로 필터링한 데이터를 파일에 저장
data.to_csv('./movies_metadata.csv', index = False)

#비슷한 콘텐츠를 추천 (ex. 장르)

"""CountVectorizer : 문서에서 단어의 빈도수를 계산하여 문서 단어 행렬을 생성
    문서를 토큰 리스트로 변환
    각 문서에서 토근의 출현 빈도를 셈
    각 문서를 BOW인코딩 벡터로 변환
"""

print(data.genres.head(2))
#ngram_range(min, max) : 단어장 생성에 사용할 토큰의 크기
count_vector = CountVectorizer(ngram_range = (1, 3))
c_vector_genres = count_vector.fit_transform(data['genres'])
print(c_vector_genres.shape)

#cosine similarity
#코사인 유사도 + vote_count가 높은 것 기반으로 추천
genre_c_sim = cosine_similarity(c_vector_genres, c_vector_genres).argsort()[:, ::-1] #내림차순
print(genre_c_sim.shape)

def get_recommend_movie_list(df, movie_title, top=30):
    target_movie_index = df[df['title'] == movie_title].index.values
    #reshape : 기존 데이터 유지, 차원과 형상을 변경 (-1: 자동)
    sim_index = genre_c_sim[target_movie_index, :top].reshape(-1)
    sim_index = sim_index[sim_index != target_movie_index]

    #iloc : 위치기반 찾기
    #sort_values : 컬럼을 기준으로 정렬
    result = df.iloc[sim_index].sort_values('score', ascending = False)[:10] #역순정렬
    return result
print('====')

print(get_recommend_movie_list(data, movie_title = 'The Dark Knight Rises'))

print(data[data['title'] == 'The Dark Knight Rises'])
