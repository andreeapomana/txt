# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:07:17 2019

@author: AdrianGigi
"""


import nltk

f = open("NASA.txt", encoding="utf8")
text = f.read()


nltk.download('punkt')

tokens = nltk.word_tokenize(text)
print(tokens)

 from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
 wnl = WordNetLemmatizer()
 for i in tokens:
     print(i, wnl.lemmatize(i))
     
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(tokens)


nltk.download('brown')
 text = nltk.Text(word.lower() for word in nltk.NASA.brown.words())
text.similar('eat')


text = nltk.Text(tokens)
type(text)  
words = [w.lower() for w in text if w.isalpha()]

from nltk.probability import FreqDist
fdist = FreqDist(words)
top_oneh = fdist.most_common(5)
print(top_oneh)


 	

>>> from nltk.NASA import brown
>>> brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
nltk.download('universal_tagset')
>>> tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
>>> tag_fd.most_common()

