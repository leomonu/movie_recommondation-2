import enum
from numpy.core.numeric import indices
import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df  = pd.read_csv("final.csv")
df  = df[df["soup"].notna()]
count=  CountVectorizer(stop_words="english")
countMatrix = count.fit_transform(df["soup"]) 
cosine_sim = cosine_similarity(countMatrix,countMatrix)

df = df.reset_index()
indices = pd.Series(df.index,index = df["title"])
def get_recommondation(title):
    idx = indices[title]
    sim_score = list(enumerate(cosine_sim[idx]))
    sim_score = sorted(sim_score,key = lambda x:x[1],reverse = True)
    sim_score = sim_score[1:11]
    movies_indices = [i[0]for i in sim_score]
    return df[["title","poster_link","release_data","runtime","vote_average","overview"]].iloc[movies_indices].values.tolist()
    
