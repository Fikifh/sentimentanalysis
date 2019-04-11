import re
import csv
from nltk.tokenize import word_tokenize

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

def fillKamus(filename):
    file_data = open(filename)
    kamus = {}
    file_data.readline()
    for key in file_data:
        key = key.replace('"', '').strip()
        k = key.split(",")
        kamus['%s' % k[0]] = '%s' % k[1]
    return kamus
kamusSlang = fillKamus('kamus-kata-tidak-baku.csv')       

with open('sentimenprabowo.csv', "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    a=-1   
    # untuk menyimpan perubahan
    f = open('sentimenprabowopreproses.csv', 'w')
    w = csv.writer(f)
    for row in reader: 
        barisdata = row[3]
        token = barisdata.split()                       
        line = trans(token, kamusSlang)
        print(line) 
        w.writerow(line)
    f.close()