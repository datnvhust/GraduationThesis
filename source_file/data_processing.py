from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from gensim.parsing.preprocessing import STOPWORDS
import re

def pre_processing(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    f.close()
    sentences = []
    for newline in lines:
        x = []
        line = re.sub(r'\W', ' ', newline)
        line = re.sub(r'\d', '', line)
        line = re.sub('_', ' ', line)
        words = word_tokenize(line)
        if len(line) <= 1:
            continue
        for word in words:
            if len(word)==1:
                continue
            if word.islower() == True:
                x.append(word)
            elif word.isupper() == True:
                x.append(word.lower())
            else:
                char = []
                for i in range(0, len(word)):
                    if word[i].islower() == True:
                        char.append(word[i])
                    else:
                        char.append(' ')
                        char.append(word[i])
                for ptu in word_tokenize(''.join(char)):
                    if len(ptu) > 1:
                        x.append(ptu.lower())

    if len(x) != 0:
            sentences.append(x)
    return  sentences

def split_word(word):
    arr_split=[]
    w=""
    i=1
    while(i<len(word)):
        if i==len(word)-1:
            arr_split.append(word[:i+1])
        if ord(word[i])<97:
            arr_split.append(word[:i])
            word=word[i:]
            i=1
            continue
        i+=1
    arr_split=[w.lower() for w in arr_split if w not in STOPWORDS]
    arr_split=[w for w in arr_split if len(w)!=1]
    return arr_split
