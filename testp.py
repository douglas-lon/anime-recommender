import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pre_preocessing import remove_useless_data_and_nan, text_preprocessing

animes = pd.read_csv('./anime.csv', sep=',')
cV = CountVectorizer()
n = animes[animes['Name'].str.contains('Naruto')]

def do(x):
    x = x.lower()
    x = x.replace(',', '')
    return x

df = pd.DataFrame()
df['Name'] = n['Name'].values
df['Tags'] = n['Tags'].values
df['Tags'] = df.Tags.apply(lambda x: do(x))
print(df)

df_p = cV.fit_transform(df.Tags)

cosine = cosine_similarity(df_p)
kj = list(enumerate(cosine[1]))

kj.sort()

for i in range(0,5):

    print(df.loc[kj[i][0]])
