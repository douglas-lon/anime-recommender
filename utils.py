import pandas as pd

def match_name(name, df):
    matching_names = pd.DataFrame()
    matching_names['Name'] = df[df.Name.str.contains(name.strip())].Name
    
    return matching_names

def search_similar(anime_index, cosine_list):
    cosine_similarity_by_index = list(enumerate(cosine_list[anime_index]))

    similarity = pd.DataFrame(cosine_similarity_by_index, columns=['Rank', 'Similarity'])
    similarity = similarity.sort_values(by=['Similarity'], ascending=False)

    return similarity

def show_similar(similarity_df, anime_df, qtd):
    count = 0
    row_list = []
    for i, row in similarity_df.iterrows():
        row = {
            'Similarity': row.Similarity,
            'Name': anime_df.loc[row.Rank].Name,
            'Description': anime_df.loc[row.Rank].Description
        }
        
        row_list.append(row)
        count += 1
        if count > qtd:
            break

    show_df = pd.DataFrame(row_list)

    print(show_df)