# coding: utf-8

# task 2

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv('train_likes.csv')

with open('items.json') as q:
    items_dicts = json.load(q) #list
    
genres = [] #list of genres
i = 0
for el in items_dicts:
    genres.append(el[u'genre'])
    i += 1
print list(set(genres))


#print type(unicode(data['item_id'][1]))
#print type(genres_films[1][1])

#while(i < len(genres)):
    #num_likes = 0
    #for el in genres_films[i]:
    #    for x in data['item_id']:
    #        if el == unicode(x):
                #print type(unicode(x)), type(el)
    #            num_likes += 1
                #print num_likes
    #genres_likes[i] = num_likes
    #i += 1
#print genres_likes[0]
#print len(genres)
