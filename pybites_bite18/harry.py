import os
import urllib.request
from collections import Counter
import re 

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    stop_words = [
        line.strip()
        for line in open(stopwords_file)
    ]

    _txt = [
        line.strip().lower()
        for line in open(harry_text)
    ]
    _txt = [' '.join(re.findall('[a-z\'s ]+', line))  for line in _txt]
    text = ' '.join(_txt)

    word_list = [
        word 
        for word in text.split() 
        if word not in stop_words and len(word) > 1
    ]

    return Counter(word_list).most_common()[0]