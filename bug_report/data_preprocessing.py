from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from gensim.parsing.preprocessing import STOPWORDS
import pandas as pd
import re
from nltk import sent_tokenize,word_tokenize

def processing(row):
    ps = PorterStemmer()
    y_save = []
    if (type(row)==str):
        x = sent_tokenize(row)
        line_after = ''
        for y1 in x:
            y1 = re.sub(r'\W', ' ', y1)  # remove 
            y1 = re.sub(r'\d', ' ', y1)  # remove digits
            words = word_tokenize(y1)
            words=[w for w in words if w not in STOPWORDS]
            words=[w.lower() for w in words]
            for w1 in words:
                if (len(w1) != 1):  # if w1 is a character then delete
                    w1 = ps.stem(w1)
                    line_after += ' '
                    line_after += w1
            # line_after += '.'
        y_save.append(line_after.lower())
    else:
        y_save.append('')
    return y_save
