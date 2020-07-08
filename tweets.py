# Open/Create a file to append data
import csv
csvFile = open('blm_final1.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
#Extracting tweets about #BlackLiveMatters and writing into a csv file. 
# '-filter:retweets' used to filter out retweets.
for tweet in tweepy.Cursor(api.search,q='#MNITagainstExams -filter:retweets',count=200,lang="en", tweet_mode='extended',since="2020-06-01").items():
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
        print (tweet.created_at, tweet.full_text)
        csvWriter.writerow([tweet.created_at, tweet.full_text]) #Code block to double check that retweets are not written in the csv file.
