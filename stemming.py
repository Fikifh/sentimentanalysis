import json
from nltk.corpus import stopwords
import pandas as pd


class stemm():


def stem(self, data):
    df = pd.read_csv('sentimenprabowo.csv', encoding='latin-1')

    print('--- Print the Basic info if the data ---')
    print(df.info)
    print(df.shape)

    print('---Pint the head/Tail of the data----')
    print(df.head())
    print('-------------------------')
    print(df.tail())

    short_data = df.head()
    stop = stopwords.words('indoensia')

    print(short_data['tweet'])
    print('-----------removing stop word-------------')
    short_data['step1_tweet'] = short_data['tweet'].apply(
        lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    print(short_data['step1_tweet'])
