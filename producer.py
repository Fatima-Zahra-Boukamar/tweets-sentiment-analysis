import tweepy
from textblob import TextBlob
from kafka import KafkaProducer
import json


BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAL0M1AEAAAAApk6m%2BLswEsei4jBts4Rh2KgUJjY%3DaQr6kJ0Q9Vo3ZEaIXQjkWft0J52CiVfplibATZst9a8RePSNYR"

# Set up Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda k: json.dumps(k).encode('utf-8')
)

# Set up Tweepy client (API v2)
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Search tweets using API v2 (up to 100 recent tweets)
query = "trump -is:retweet lang:en"  # Exclude retweets and non-English tweets
response = client.search_recent_tweets(query=query, max_results=10)

# Process and send each tweet
if response.data:
    for tweet in response.data:
        text = tweet.text
        print(text)

        # Sentiment analysis using TextBlob
        analysis = TextBlob(text)
        sentiment = analysis.sentiment.polarity

        message = {
            "text": text,
            "sentiment": sentiment
        }

        producer.send('tweets', message)

    producer.flush()
else:
    print("No tweets found.")
