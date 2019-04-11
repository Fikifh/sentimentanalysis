import nltk
nltk.download()
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd


data = pd.read_csv('../sentimenprabowo.csv', encoding='latin-1')

stop_words = set(stopwords.words('id'))

data_tweet = data.head()

word_tokens = word_tokenize(data_tweet['tweet'])

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print('==============================================================')
print(filtered_sentence)


print('--------Basic Info of the Data---------')
print(data.info())
print(data.shape())

print('--------Head/Tail of data---------')
print(data.head())

print('-----------------------------------')
print(data.tail())

