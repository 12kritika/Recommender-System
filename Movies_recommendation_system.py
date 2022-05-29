#Movies Recommendation System

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity

#Data Collection and preprocessing

movies_data= pd.read_csv("movies.csv")

movies_data.head()
movies_data.shape

#Selecting relevant features
df = movies_data[['genres','keywords','tagline','cast','director']].copy()
df.tail()

df.shape
df.isnull().sum()
df.fillna('', inplace=True)


df_concat= df['genres']+' ' + df['cast'] + ' ' +df['director']+ ' '+ df['keywords']+ ' ' + df['tagline']
print(df_concat)

#convert text data to feature vector
feature_vector= TfidfVectorizer().fit_transform(df_concat)

print(feature_vector)
#cosine similarity
similarity = cosine_similarity(feature_vector)


#getting movie input from user
movie_name = input("Enter movie name")

title_name= movies_data['original_title'].values
title_name

#Finding the index of movie with title (while searching for movie it should be linked with itle otherwise sorting could change the index)
index = movies_data[movies_data['title']== movie_name]['index'].values[0]




print(similarity_score)

# sorting the movies based on similarity score
sorted_value= sorted(similarity_score, key =lambda x: x[1], reverse=True)
print(sorted_value)

#print recommended movies
print ('top recommended movies \n')

i=0
for movie in sorted_value:
  title_from_index= movies_data[movies_data['index']==movie[0]]['title'].values[0]
  if i<6 and i>=1 :
    print(i,title_from_index)
  i+=1
