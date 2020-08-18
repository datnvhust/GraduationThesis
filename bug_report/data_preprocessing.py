from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from gensim.parsing.preprocessing import STOPWORDS
import pandas as pd
import re
from nltk import sent_tokenize,word_tokenize
import numpy as np
import nltk
nltk.download('punkt')

def processing(row):
    ps = PorterStemmer()
    y_save = []
    x = sent_tokenize(row)
    line_after = ''
    for y1 in x:
        y1 = re.sub(r'\W', ' ', y1)  # loại bỏ kí tự đặc biệt 
        y1 = re.sub(r'\d', ' ', y1)  # loại bỏ số
        words = word_tokenize(y1)
        words=[w for w in words if w not in STOPWORDS]
        words=[w.lower() for w in words]
        for w1 in words:
            if (len(w1) != 1):  # nếu w1 là 1 từ có 1 kí tự thì loại bỏ
                w1 = ps.stem(w1)
                line_after += ' '
                line_after += w1

    y_save.append(line_after.lower())
    return y_save

# def get_data(data):
#     data_summary=data["summary"]
#     data_description=data["description"]
#     files=np.array([[]])
#     for summary, desc in zip(data_summary, data_description):
#         if not desc or pd.isnull(desc):
#             continue
#         try:
#             summary=processing(summary)
#             summary=''.join(summary)
#             print("summary ", summary )
#             desc=processing(desc)
#             desc=''.join(desc)
#             print("desc ", desc)
#         except:
#             continue
#     return files

data = pd.read_csv('../Dataset/dataset/AspectJ.csv')
# get_data(data)