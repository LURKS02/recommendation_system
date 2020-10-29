from sklearn.decomposition import TruncatedSVD
from scipy.sparse.linalg import svds

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def mat_recommend(movieName):
	rating_data = pd.read_csv('./ratings.csv')
	movie_data = pd.read_csv('./movies_test.csv')

	rating_data.drop('timestamp', axis = 1, inplace = True)

	movie_data.drop('genres', axis = 1, inplace = True)

	user_movie_data = pd.merge(rating_data, movie_data, on = 'movieId')

	user_movie_rating = user_movie_data.pivot_table('rating', index = 'userId', columns='title').fillna(0)


	movie_user_rating = user_movie_rating.values.T

	type(movie_user_rating)

	SVD = TruncatedSVD(n_components = 12)
	matrix = SVD.fit_transform(movie_user_rating)

	matrix[0]

	corr = np.corrcoef(matrix)
	corr2 = corr[:200, :200]

	plt.figure(figsize = (16,10))

	movie_title = user_movie_rating.columns
	movie_title_list = list(movie_title)
	coffey_hands = movie_title_list.index(movieName)

	corr_coffey_hands = corr[coffey_hands]

#=============================================================================

	df_ratings = pd.read_csv('./ratings.csv')
	df_movies = pd.read_csv('./movies.csv')

	df_user_movie_ratings = df_ratings.pivot(
	    index='userId',
	    columns='movieId',
	    values='rating'
	).fillna(0)

	matrix = df_user_movie_ratings.to_numpy()
	user_ratings_mean = np.mean(matrix, axis = 1)
	matrix_user_mean = matrix - user_ratings_mean.reshape(-1,1)

	pd.DataFrame(matrix_user_mean, columns = df_user_movie_ratings.columns).head()


	U, sigma, Vt = svds(matrix_user_mean, k = 12)

	sigma = np.diag(sigma)

	svd_user_predicted_ratings = np.dot(np.dot(U, sigma),Vt) + user_ratings_mean.reshape(-1,1)
	df_svd_preds = pd.DataFrame(svd_user_predicted_ratings, columns = df_user_movie_ratings.columns)


	return (list(movie_title[(corr_coffey_hands >= 0.9)]))
	
def movie_info(recommend_title, base_title):
	mat = mat_recommend(base_title)
	return mat[mat['title'] == recommend_title]
