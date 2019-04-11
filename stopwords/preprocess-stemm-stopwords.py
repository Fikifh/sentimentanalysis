from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

import pandas as pd
import re
import csv

factorySW = StopWordRemoverFactory()
factoryST = StemmerFactory()

stopword = factorySW.create_stop_word_remover()
stemmer = factoryST.create_stemmer()

# process the tweets
def processTweet(tweet):            
    # Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    # Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    # remove rt
    tweet = re.sub('rt','', tweet)
    # Convert to lower case
    tweet = tweet.lower()
    # Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    # Convert @username to AT_USER
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    # trim
    tweet = tweet.strip('\'"')
    # remove rt
    tweet = re.sub('rt','', tweet)
    # Convert to lower case
    tweet = tweet.lower()    
    return tweet
    # end

# kalimat
data = pd.read_csv('../sentimenprabowo.csv', encoding='utf8')
data_tweet = data.head()

#untuk membuka csv
#fp = open('../sentimenprabowo.csv', 'r', encoding="utf8")
#line = csv.reader(fp)

#untuk menyimpan ke csv
f = open('../sentimenprabowopreproses.csv', 'w', encoding="utf8")
w = csv.writer(f)
w.writerow(('tweet'))
print('==============================')
print('==== Melakukan preprocess ======')
print('==== Melakukan Stopword ======')
print('==== Melakukan Stemmer =======')
print('==============================')
#for row in line:
    # preprocess = processTweet(row[3])
    # stop = stopword.remove(preprocess)
    # katadasar = stemmer.stem(stop)     
    # print(katadasar)  
    # w.writerow(katadasar)    

for row in data_tweet['tweet']:        
    preprocess = processTweet(row)
    katadasar = stemmer.stem(preprocess)
    stop = stopword.remove(katadasar)          
    w.writerow(stop)       
    print(katadasar)