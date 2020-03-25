

# In[2]:


import tweepy
import csv
import pandas as pd

consumer_key = 'Enter consumer key within single quotes'
consumer_secret = 'Enter consumer secret key within single quotes'
access_token = 'Enter access token key within single quotes'
access_token_secret = 'Enter secret access key within single quotes'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('tweets.csv', 'w')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#AyodhyaVerdict",count=100,
                           lang="en",
                           since="2019-11-28").items():
    #print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.user.screen_name, tweet.text.encode('utf-8')])

csv = pd.read_csv('tweets.csv',names=["Username","Tweet"])
count = csv['Username'].value_counts()[:]
csv.head(10)

top2 = count.head(2)
top2

import matplotlib.pyplot as plt
colors =  ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]
top2.plot.pie(y=top2.index,
           shadow=False,
           colors=colors, 
           radius = 1000,
           explode=(0, 0),   
           startangle=90,
           autopct='%1.1f%%',
           textprops={'fontsize': 10})

plt.axis('equal')
plt.tight_layout()
plt.show()


# In[3]:


csv





