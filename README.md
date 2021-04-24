# Dogecoin Twitter Analysis
This is a public repository in case anyone is interested in analyzing the recent dogecoin trends using Twitter data. Through textual analysis of Twitter tweets, we can better understand the volatility of Dogecoin through how people are talking about it.

## About DogeCoin
Dogecoin (DOGE) is an alt-coin based on the doge meme featuring a Shiba Inu. Although Dogecoin was initially created as a meme and had stagnant growth, it's popularity and value has surged in recent months. In mid April, Dogecoin peaked at $0.44 / DOGE, making it the 4th most valuable cryptocurrency by market cap.

## Requirements and libraries
* Python 3.8 (this may not work on other versions)
* snscraper development version (https://github.com/JustAnotherArchivist/snscrape) 
* pandas
* numpy
* TextBlob
* MathPlotLib

## Files
### scraper.py
Used to get historical tweets from Twitter. Some other libraries are currently unstable and Tweepy does not allow you to search for historical tweets older than 7 days ago.

This file automates the collection of up to 2000 tweets (if available) and collects the following information:
* ID
* Date
* Content
* Number of replies
* Number of retweets
* Number of likes
* Number of quotes
