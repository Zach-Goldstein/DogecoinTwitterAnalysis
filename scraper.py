import csv
import snscrape.modules.twitter as sntwitter
import datetime as dt
import time
# Generating datetime objects
from datetime import datetime, timedelta

def get_tweets_on_date(start_day):
    keyword = 'dogecoin OR Dogecoin OR DogeCoin'
    maxTweets = 2000
    end_day = start_day + timedelta(days = 1)

    #Open/create a file to append data to
    csvFile = open('dogecoin-sentiment-' + start_day.strftime('%Y-%m-%d') + '.csv', 'w', newline='', encoding='utf8')

    #Use csv writer
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['id','date','text','user','replyCount','retweetCount','likeCount','quoteCount'])

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' lang:en since:' +  start_day.strftime('%Y-%m-%d') + ' until:' + end_day.strftime('%Y-%m-%d') + ' -filter:links -filter:replies').get_items()):
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.id, tweet.date, tweet.content, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount])
    csvFile.close()

start_date = dt.date(2021, 1, 1)
end_date = dt.date(2021, 4, 22)
delta = timedelta(days = 1)

while start_date <= end_date:
    print(start_date)
    get_tweets_on_date(start_date)
    start_date += delta
