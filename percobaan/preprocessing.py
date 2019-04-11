import csv
import re, string

dataset = open('../sentimenprabowo.csv', 'r')
sentiment = csv.reader(dataset, delimiter=',')

newDok = open('../sentimenprabowopreproses.csv', 'w')
save = csv.writer(newDok)

DATA_KBBI 	= []
DATA_KBBI	= [kamus.strip('\n').strip('\r') for kamus in open('kbbi.txt')]

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
    tweet = re.sub('@[^\s]+', 'ATUSER', tweet)
    # trim
    tweet = tweet.strip('\'"')
    # remove rt
    tweet = re.sub('rt','', tweet)
    # Convert to lower case
    tweet = tweet.lower() 
    #hapus angka dan angka yang berada dalam string 
    tweet = re.sub(r'\w*\d\w*', '',tweet).strip() 
    #hapus punctuation dalam kata
    tweet = re.sub(r'[^\w\s]','',tweet)
    #delete puctuation
    tanda_baca = set(string.punctuation)
    tweet = ''.join(ch for ch in tweet if ch not in tanda_baca)    
    return tweet
#end

def kbbi(token): 
    global DATA_KBBI

    #ubah list menjadi dictionary 
    dic={}
    for i in DATA_KBBI: 
        (key,val)=i.split('\t')
        dic[str(key)]=val

    #kbbi cocokan 
    final_string = ' '.join(str(dic.get(word, word)) for word in token)
    return final_string

for row in sentiment:
    tweet = row[3]
    normalize = processTweet(tweet).split()
    pre = kbbi(normalize)
    print(pre)