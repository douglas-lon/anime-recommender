import numpy as np

def remove_useless_data_and_nan(df):

    df = df[(df.Name == '[email protected]') == False]
    df.drop(columns=['End_year', 'Voice_actors', 'staff', 'Release_season', 'Release_year'], inplace=True)

    numeros = df.select_dtypes(include=np.number)
    colunas_numerica = numeros.columns
    df[colunas_numerica] = df[colunas_numerica].fillna(df.mean())
    df.fillna(method='ffill', inplace=True)

    df.reset_index(drop=True)

    return df

def text_preprocessing(df):
    def do(x):
        x = x.lower()
        x = x.replace(',', '')
        return x

    df['Tags'] = df.Tags.apply(lambda x: do(x))

    return df['Tags']