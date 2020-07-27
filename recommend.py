from sklearn.decomposition import TruncatedSVD
from scipy.sparse.linalg import svds

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

rating_data = pd.read_csv('./ratings.csv')
movie_data = pd.read_csv('./movies.csv')

print(rating_data.head())
print(movie_data.head())
print(movie_data.shape)
print(rating_data.shape)

rating_data.drop('timestamp', axis = 1, inplace = True)
print(rating_data.head())

movie_data.drop('genres', axis = 1, inplace = True)
print(movie_data.head())

user_movie_data = pd.merge(rating_data, movie_data, on = 'movieId')
print(user_movie_data.head())
print(user_movie_data.shape)

user_movie_rating = user_movie_data.pivot_table('rating', index = 'userId', columns='title').fillna(0)

print(user_movie_rating.shape)
print(user_movie_rating.head())

movie_user_rating = user_movie_rating.values.T
print(movie_user_rating.shape)

type(movie_user_rating)

SVD = TruncatedSVD(n_components = 12)
matrix = SVD.fit_transform(movie_user_rating)
print(matrix.shape)

matrix[0]

corr = np.corrcoef(matrix)
print(corr.shape)

corr2 = corr[:200, :200]
print(corr2.shape)

plt.figure(figsize = (16,10))
print(sns.heatmap(corr2))

movie_title = user_movie_rating.columns
movie_title_list = list(movie_title)
coffey_hands = movie_title_list.index("Guardians of the Galaxy (2014)")

corr_coffey_hands = corr[coffey_hands]
list(movie_title[(corr_coffey_hands >= 0.9)])[:50]



df_ratings = pd.read_csv('./ratings.csv')
df_movies = pd.read_csv('./movies.csv')

df_user_movie_ratings = df_ratings.pivot(
    index='userId',
    columns='movieId',
    values='rating'
).fillna(0)

print(df_user_movie_ratings.head())

matrix = df_user_movie_ratings.to_numpy()
user_ratings_mean = np.mean(matrix, axis = 1)
matrix_user_mean = matrix - user_ratings_mean.reshape(-1,1)

print(matrix)
print(matrix.shape)
print(user_ratings_mean.shape)
print(matrix_user_mean.shape)
pd.DataFrame(matrix_user_mean, columns = df_user_movie_ratings.columns).head()


U, sigma, Vt = svds(matrix_user_mean, k = 12)

print(U.shape)
print(sigma.shape)
print(Vt.shape)

sigma = np.diag(sigma)
print(sigma.shape)
print(sigma[0])
print(sigma[1])

svd_user_predicted_ratings = np.dot(np.dot(U, sigma),Vt) + user_ratings_mean.reshape(-1,1)
df_svd_preds = pd.DataFrame(svd_user_predicted_ratings, columns = df_user_movie_ratings.columns)
print(df_svd_preds.head())
print(df_svd_preds.shape)



def recommend_movies(df_svd_preds, user_id, ori_movies_df, ori_ratings_df, num_recommendations=5):
	user_row_number = user_id - 1
	sorted_user_predictions = df_svd_preds.iloc[user_row_number].sort_values(ascending=False)
	user_data = ori_ratings_df[ori_ratings_df.userId == user_id]
	user_history = user_data.merge(ori_movies_df, on = 'movieId').sort_values(['rating'], ascending=False)
	recommendations = ori_movies_df[~ori_movies_df['movieId'].isin(user_history['movieId'])]
	recommendations = recommendations.merge( pd.DataFrame(sorted_user_predictions).reset_index(), on = 'movieId')
	recommendations = recommendations.rename(columns = {user_row_number: 'Predictions'}).sort_values('Predictions', ascending = False).iloc[:num_recommendations, :]

	return user_history, recommendations

already_rated, predictions = recommend_movies(df_svd_preds, 330, df_movies, df_ratings, 10)
print(already_rated.head(10))
print(predictions)
