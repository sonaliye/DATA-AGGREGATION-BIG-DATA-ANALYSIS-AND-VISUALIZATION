import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'eE9Pk3sp9U2hTitMAB4AYuKbA'
consumer_secret = '2uSAVDuSoNz9QiERL8ctzA1R9AkTWjiYCJBzebT5OPtJucgExf'
access_token = '1094424866944630785-WEelD8vOhkDPlkIkCQtgzIDRE3zEef'
access_token_secret = 'E9cfhZvDyC3e8qXIxFgCwGTcpEiSp6hW0B2r4C2Rog1TD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('badminton.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
tweetCount = 1000
query = "badminton"
since_date="2019-03-01"
for tweet in tweepy.Cursor(api.search,q=query,count=tweetCount,
                           lang="en",
                           since=since_date).items(100):
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at,tweet.user.screen_name, tweet.text.encode('utf-8')])