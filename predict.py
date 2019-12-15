# -*- coding: utf-8 -*-
import pickle
import sys
import analysis
import pandas as pd
from gensim import corpora
from gensim.corpora import Dictionary

args = sys.argv

with open('model.pickle', mode='rb') as fp:
    clf = pickle.load(fp)

predict2word = ['見る価値なし', 'まあまあ', '一見の価値あり']

dictionary = Dictionary.load('data/jarujaru.dict')

title = args[1]
test_words = analysis.get_words([title])
test_dense = [analysis.vec2dense(dictionary.doc2bow(test_words[i]),len(dictionary)) for i in range(len(test_words))]
predicted0 = clf.predict(test_dense)
print(predict2word[predicted0[0]])
