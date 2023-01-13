import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pre_preocessing import remove_useless_data_and_nan, text_preprocessing
from utils import match_name, search_similar, show_similar

animes_data = pd.read_csv('./anime.csv', sep=',')
cV = CountVectorizer()

animes_data = remove_useless_data_and_nan(animes_data)

animes = pd.DataFrame()
animes['Name'] = animes_data['Name'].values
animes['Tags'] = animes_data['Tags'].values
animes['Description'] = animes_data['Description'].values
animes['Tags'] = text_preprocessing(animes)

animes_word_vector = cV.fit_transform(animes.Tags)
cosine = cosine_similarity(animes_word_vector)

animes_name = input('Digite o nome do anime: ')
matching_names = match_name(animes_name, animes)
print('ANIMES COM NOME PARECIDO')
print(matching_names)
anime_index = int(input('Digite o número do anime: '))

similarity = search_similar(anime_index, cosine)
show_similar(similarity, animes, 5)

