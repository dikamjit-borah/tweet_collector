import tweepy
 
import pandas as pd
import csv
import re 
import string
import preprocessor as p
import time
import random

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_TOKEN")
auth.set_access_token("ACCESS_KEY", "ACCESS_TOKEN")

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text.encode('utf-8'))


csvFile = open('bts_india2.csv', 'a', newline='')
csvFile2 = open('bts_world2.csv', 'a', newline='')
csvWriter = csv.writer(csvFile)
csvWriter2 = csv.writer(csvFile2)

search_words = "bts"     
new_search = search_words + " -filter:retweets"
COUNT = 0
print("Fetching...")
substring = "India"
count =0
for tweet in tweepy.Cursor(api.search,q=new_search,count=100,lang="en",since_id=0, exclude='retweets', geo_enabled=True, wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items():
    if(count<100):
        count = count + 1
        print("####################################")
        print("{} -> {}".format(count, tweet.id_str))
        time.sleep(random.randint(2, 8))
        T_ID=tweet.id_str
        T_TEXT = tweet.text.encode('utf-8')
        T_DATETIME = tweet.created_at
        T_USERNAME = tweet.user.name.encode('utf-8')
        T_SCREENNAME = tweet.user.screen_name.encode('utf-8')
        T_LOCATION = tweet.user.location.encode('utf-8')
        T_FOLLOWERS = tweet.user.followers_count
        T_FRIENDS = tweet.user.friends_count
        T_STATUSES = tweet.user.statuses_count
        T_HASHTAGS = []
        T_MENTIONS = []
        try:
            for i in range(3):
                T_HASHTAGS.append(tweet.entities["hashtags"][i]["text"])
        except:
            pass
           
        try:
            for i in range(3):
                T_MENTIONS.append(tweet.entities["user_mentions"][i]["screen_name"].encode('utf-8'))
        except:
            pass

        if(len(tweet.entities["hashtags"])>0 and substring in tweet.user.location):
            if(COUNT<50):
                #print(tweet)
                #if(tweet.user.location.startswith("b''", 0, 3)==False):
                #print(COUNT)
                try:
                    print("Writing in bts_india")    
                    csvWriter.writerow([T_ID, T_DATETIME, T_TEXT, T_HASHTAGS, T_MENTIONS, T_LOCATION, T_USERNAME, T_SCREENNAME, T_FOLLOWERS, T_FRIENDS, T_STATUSES ])
                    COUNT = COUNT + 1
                    print("bts_india comments = ".format(COUNT))
               
                except:
                    pass
            
            else:
                exit()
        else:
            try:
                print("Writing in bts_world")
                csvWriter2.writerow([T_ID, T_DATETIME, T_TEXT, T_HASHTAGS, T_MENTIONS, T_LOCATION, T_USERNAME, T_SCREENNAME, T_FOLLOWERS, T_FRIENDS, T_STATUSES ])
                print("bts_world comments = ", count)

            except:
                pass
        print("####################################")
        print("")
    else:
        exit()

