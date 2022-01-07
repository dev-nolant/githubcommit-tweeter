import tweepy
# personal information
consumer_key = 'abc'
secret = 'abc'
token = 'abc'
token_secret = 'abc'

auth = tweepy.OAuthHandler(consumer_key, secret)
auth.set_access_token(token, token_secret)


def send_tweet(quote: str):
    api = tweepy.API(auth)
    # Authentication of access token and secret
    for tweet in tweepy.Cursor(api.user_timeline).items():
        if quote in tweet.text:
            return 0
        else:
            continue
    api.update_status(str(quote))
    return 1
