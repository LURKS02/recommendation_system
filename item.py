import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('./ratings_small.csv')
print(data.head())

data = data.pivot_table('rating', index = 'userId', columns = 'movieId')
print(data.head())
print(data.shape)

ratings = pd.read_csv('./ratings_small.csv')
movies = pd.read_csv('./movies_metadata.csv')
#자료형 일치
#movies['id'] = movies['id'].astype(int)
#dataframe 컬럼명 바꾸기 : .rename(columns = { : })
movies.rename(columns = {'id':'movieId'}, inplace = True)
ratings_movies = pd.merge(ratings, movies, on = 'movieId')
print(ratings_movies.head(1))
print(ratings_movies.shape)

#fillna() : 결손 데이터 대치
data = ratings_movies.pivot_table('rating', index = 'userId', columns = 'title').fillna(0)
print(data.head())
print(data.shape)
#.transpose : 행열반전
data = data.transpose()
print(data.head(2))
print(data.shape)

movie_sim = cosine_similarity(data, data)
print(movie_sim.shape)

#행렬 형태로 비교하기 위함
movie_sim_df = pd.DataFrame(data = movie_sim, index = data.index, columns = data.index)
print(movie_sim_df.head(3))

print(movie_sim_df["X-Men Origins: Wolverine"].sort_values(ascending=False)[1:10])
print(movie_sim_df["Harry Potter and the Half-Blood Prince"].sort_values(ascending=False)[1:10])
print(movie_sim_df["King Kong"].sort_values(ascending=False)[1:10])

print("====")

rating_data = pd.read_csv('./ratings.csv')
movie_data = pd.read_csv('./movies.csv')
print(rating_data.head(2))
print(movie_data.head(2))

#labels : 삭제하려는 index 또는 column
#axis : 0 or index = index / 1 or column = column
#inplace : 원본 데이터 수정 (True일때 수정)
rating_data.drop('timestamp', axis = 1, inplace = True)
print(rating_data.head(2))

user_movie_rating = pd.merge(rating_data, movie_data, on = 'movieId')
print(user_movie_rating.head(2))

#item based collaborative filtering
movie_user_rating = user_movie_rating.pivot_table('rating', index = 'title', columns = 'userId')
user_movie_rating = user_movie_rating.pivot_table('rating', index = 'userId', columns = 'title')

print(user_movie_rating.head(5))
print(movie_user_rating.head(5))

movie_user_rating.fillna(0, inplace = True)
print(movie_user_rating.head(3))

item_based_collabor = cosine_similarity(movie_user_rating)
print(item_based_collabor)
item_based_collabor = pd.DataFrame(data = item_based_collabor, index = movie_user_rating.index, columns = movie_user_rating.index)
print(item_based_collabor.head())

def get_item_based_collabor(title):
    return item_based_collabor[title].sort_values(ascending=False)[:6]
print(get_item_based_collabor('Godfather, The (1972)'))