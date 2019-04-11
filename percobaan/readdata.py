import csv
import re
APPOSTOPHS= {"tdk": "tidak", "yg":"yang","sy":"saya","tgl":"tanggal"}    
test_string = "sy tdk melakukan apapun tentang hal itu"

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


dataset = open('../sentimenprabowo.csv', 'r')
sentiment = csv.reader(dataset, delimiter=',')

newDok = open('../sentimenprabowopreproses.csv', 'w')
save = csv.writer(newDok)

data= open("convertcsv.txt", "r")
APPOSTOPHE=data.read()
APPOSTOPHSe = [APPOSTOPHE]
#print(APPOSTOPHES)

new_sentence = []
for row in sentiment:
    processedTweet = processTweet(row[3])
    #print(processedTweet)   
    # look for each candidate    
    for candidate_replacement in APPOSTOPHS:        
        #if our candidate is there in the word
        if candidate_replacement in processedTweet:
            # replace it 
            processedTweet = processedTweet.replace(candidate_replacement, APPOSTOPHS[candidate_replacement])
    # and pop it onto a new list 
    new_sentence.append(processedTweet)
rfrm = "\n".join(new_sentence)
print(rfrm)