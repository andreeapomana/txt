from nltk.tokenize import sent_tokenize, word_tokenize

import nltk
from nltk import punkt 

# 1) separare cuvintelor si a caracterelor

data = "Natural language processing (nlp) is a research field that presents many challenges such as natural language understanding. "

import nltk
nltk.download('punkt')

phrases = sent_tokenize(data)
words = word_tokenize(data)

print(phrases)
print(words)

# 2) identificarea partilor de vorbire

from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
from io import BytesIO

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
wnl = WordNetLemmatizer()
for i in words:
     print(i, wnl.lemmatize(i))
     
 
# 3) identificarea partilor de vorbire

   
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)


# 4) cel mai frecevent cuvant din corpus

import string
from collections import Counter
from nltk.corpus import stopwords
from collections import defaultdict, Counter
from nltk.corpus import brown
nltk.download('brown')
nltk.download('stopwords')

stoplist = stopwords.words('english')

brown = nltk.corpus.brown

from collections import defaultdict

words = brown.words()
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('language')

text=nltk.Text(words)
print(text)

#_________________________________________________________

from collections import Counter

words = words

counter_obj = Counter(words)

counter_obj.most_common() 

# 5) cea mai frecventa parte de vorbire din corpus

#realizat initial in excel


