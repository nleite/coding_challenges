#!/usr/bin/env python
import simplejson as json
import numpy as np
import string


def make_key(s):
    return s.translate(str.maketrans('', '', string.punctuation)).strip()


def make_pairs(words):
    for i in range(len(words)-1):
        yield (words[i], words[i+1])


with open('donaldtweets.json') as pf: 
    data = json.load(pf)

#print(data)
words = []
tweets = 0
word_count = 0
max_tweet_words = 0
for d in data:
    tweet_words = d['text'].split()
    tweets+=1 
    word_count= len(tweet_words)
    max_tweet_words = max(max_tweet_words, len(tweet_words) )
    words.extend(tweet_words)

pairs = make_pairs(words)

pairs_dict = {}
for p0, p1 in pairs: 
    p0 = make_key(p0)
    if p0 in pairs_dict.keys():
        pairs_dict[p0].append(p1)
    pairs_dict[p0] = [p1]


n_words = np.random.randint(int(word_count/tweets), max_tweet_words) 
chain = [ np.random.choice(words) ]

for _ in range(n_words):
    chain.append(np.random.choice(pairs_dict[make_key(chain[-1])]))

print(" ".join(chain))

