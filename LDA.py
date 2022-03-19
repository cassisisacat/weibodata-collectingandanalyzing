
from gensim import corpora
from gensim.models import LdaModel
from gensim.corpora import Dictionary
import codecs
import os
train=[]

fp=codecs.open('路径.dat','r',encoding='utf-8')
for line in fp:
  if line !='':
    line=line.split()
    train.append([w for w in line])

dictionary = corpora.Dictionary(train)

corpus =[dictionary.doc2bow(text) for text in train]

lda=LdaModel(corpus=corpus, id2word=dictionary,num_topics=10, passes=60)

for topic in lda.print_topics(num_words=20):
  termNumber=topic[0]
  print(topic[0],':',sep='')
  listOfTerms=topic[1].split('+')
  for term in listOfTerms:
    listItems=term.split('*')
    print(' ',listItems[1],'(',listItems[0],')',sep='')
