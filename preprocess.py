#import regex
import re
import csv
import unittest
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import word_tokenize

factorySW = StopWordRemoverFactory()
factoryST = StemmerFactory()

stopword = factorySW.create_stop_word_remover()
stemmer = factoryST.create_stemmer()


# function untuk preprocess tweets
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
#end

# function for tokenization
def tokenize(line):
    return filter(lambda x: x!= '', re.split('[^\w', line.lower()))

#function for translate data
def translate(line, dict):    
    #tokens = tokenize(line)
    for key,word in enumerate(line):
        if word in dict:
            line[key] = dict[word]
    return ' '.join(line)

def trans(data, kamus):
    data = []
    for key in enumerate(data):
        if key in kamus[0]:
            data = kamus[1]
        else:
            data = data
    return ' '.join(data)

def fillDict(filename):
    file_data = open(filename)
    kamus = {}
    file_data.readline()
    for key in file_data:
        key = key.replace('"', '').strip()
        k = key.split(",")
        kamus['%s' % k[0]] = '%s' % k[1]
    return kamus

kamus = fillDict('kamus-kata-tidak-baku.csv')
with open('sentimenprabowo.csv', "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    a=-1   
    # untuk menyimpan perubahan
    f = open('sentimenprabowopreproses.csv', 'w')
    w = csv.writer(f)
    with open('kamus-kata-tidak-baku.csv', "r", encoding="utf-8") as bacaKamus:
        kamusSlang = csv.reader(bacaKamus, delimiter=',')
        for row in reader:   
            #token = word_tokenize(row[3])                     
            processedTweet = processTweet(row[3])
            stop = []
            processed = [processedTweet]        
            line = trans(processed, kamusSlang)
            katadasar = stemmer.stem(line)
            stem = stopword.remove(katadasar)        
            stop = [row[0], stem]                
            print(stop) 
            w.writerow(stop)
    f.close()                
#end loop
