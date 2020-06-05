import pandas as pd
import numpy as np
from ast import literal_eval

data = pd.read_csv('./movies_metadata.csv')

data = data[['genres', 'id', 'popularity', 'title', 'vote_average', 'vote_count']]
print(data)
print(data.head(2))
print(data.shape)

""" 백분위수 구하기
quantile : 해당 백분위에 해당하는 값 (vote_count)
loc : 행단위 데이터 읽기 (인덱스 값 기준)
"""
m = data['vote_count'].quantile(0.9)
print("vote_count = " + str(m))
data = data.copy().loc[data['vote_count'] >= m]
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
#data.to_csv('./movies_metadata.csv', index = False)

