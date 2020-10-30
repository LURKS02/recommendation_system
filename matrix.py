from sklearn.decomposition import TruncatedSVD
from scipy.sparse.linalg import svds

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

def mat_recommend(input_id):
	
	input_id = int(input_id)

	rating_data = pd.read_csv('./ratings.csv')
	movie_data = pd.read_csv('./movies_test.csv')

	rating_data.drop('timestamp', axis = 1, inplace = True)
	movie_data.drop('genres',axis = 1, inplace = True)

	user_movie_data = pd.merge(rating_data, movie_data, on = 'movieId')

	user_movie_rating = user_movie_data.pivot_table('rating', index = 'userId', columns = 'title').fillna(0)

	movie_user_rating = user_movie_rating.values.T

	type(movie_user_rating)

	SVD = TruncatedSVD(n_components = 12)
	matrix = SVD.fit_transform(movie_user_rating)

	corr = np.corrcoef(matrix)
	corr2 = corr[:200, :200]
	plt.figure(figsize = (16,10))
	sns.heatmap(corr2)
	movie_title = user_movie_rating.columns
	movie_title_list = list(movie_title)
	coffey_hands = movie_title_list.index("Guardians of the Galaxy")
	corr_coffey_hands = corr[coffey_hands]
	list(movie_title[(corr_coffey_hands >= 0.9)])[:50]
	
	df_ratings = pd.read_csv('./ratings.csv')
	df_movies = pd.read_csv('./movies_test.csv')
	
	df_user_movie_ratings = df_ratings.pivot(
		index = 'userId',
		columns = 'movieId',
		values = 'rating'
	).fillna(0)
	
	matrix = df_user_movie_ratings.values
	user_ratings_mean = np.mean(matrix, axis = 1)
	matrix_user_mean = matrix - user_ratings_mean.reshape(-1,1)
	
	U, sigma, Vt = svds(matrix_user_mean, k = 12)
	
	sigma = np.diag(sigma)
	svd_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
	df_svd_preds = pd.DataFrame(svd_user_predicted_ratings, columns = df_user_movie_ratings.columns)
	
	def recommend_movies(df_svd_preds, user_id, ori_movies_df, ori_ratings_df, num_recommendations = 5):
		user_row_number = user_id - 1
		sorted_user_predictions = df_svd_preds.iloc[user_row_number].sort_values(ascending = False)
		user_data = ori_ratings_df[ori_ratings_df.userId == user_id]
		user_history = user_data.merge(ori_movies_df, on = 'movieId').sort_values(['rating'], ascending = False)
		recommendations = ori_movies_df[~ori_movies_df['movieId'].isin(user_history['movieId'])]
		recommendations = recommendations.merge(pd.DataFrame(sorted_user_predictions).reset_index(), on = 'movieId')
		recommendations = recommendations.rename(columns = {user_row_number: 'Predictions'}).sort_values('Predictions', ascending = False).iloc[:num_recommendations, :]
		return user_history, recommendations
	
	already_rated, predictions = recommend_movies(df_svd_preds, input_id, df_movies, df_ratings, 10)
	return predictions
	
def mat_recommend_title(input_id):
	movieTitleList = []
	recommend_result = mat_recommend(input_id)
	for i in range(10):
		movieTitleList.append(recommend_result.iloc[i]['title'])
	return movieTitleList
