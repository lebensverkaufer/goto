# coding: utf-8

# task 1

import json
import pandas as pd
from collections import Counter

data = pd.read_csv('train_likes.csv')
data.head()

print "Average channel like amount"
print float(data['channel'].count())/data['channel'].drop_duplicates().count()

films = Counter()
for s in data['item_id']:
    films[s] += 1

films_likesmore5 = 0
for el in films.values():
    if el >=5:
        films_likesmore5 += 1
print 'Films with 5+ likes:'
print films_likesmore5
