import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

MONTHS = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}


tweets = pickle.load(open("trumpSinceElection.dat", "rb"))
# Task 1: Count how many tweets are from different sources
sources = {}
corona = {}
print(tweets[0])
dates = []
for tweet in tweets:
    source = tweet['source']
    if not source in sources:
        sources[source] = 0
    sources[source] += 1

    if 'corona' in tweet['text'] or 'virus' in tweet['text']:
        fields = tweet['created_at'].split()
        year = fields[-1]
        if year == "2019":
            print(tweet['text'])
        month = MONTHS[fields[1]]
        day = int(fields[2])
        week_num = int(np.floor(day/7))+1
        date = "{}/{}/{}".format(year, month, week_num)
        if not date in corona:
            corona[date] = 0
        corona[date] += 1

N = len(corona)
xticks = sorted(corona.keys())
vals = [corona[x] for x in xticks]
plt.bar(range(N), vals)
plt.xticks(range(N), xticks, rotation=90)
plt.tight_layout()
plt.show()

N = len(sources)
plt.bar(range(N), list(sources.values()))
plt.xticks(range(N), list(sources.keys()), rotation=90)
plt.tight_layout()
plt.show()

retweet_counts = np.zeros(len(tweets))
favorite_counts = np.zeros(len(tweets))
dates = []
for i, tweet in enumerate(tweets):
    retweet_counts[i] = tweet['retweet_count']
    favorite_counts[i] = tweet['favorite_count']

plt.hist(favorite_counts, bins=100)
plt.show()

idx = np.argmax(favorite_counts)
print(tweets[idx])