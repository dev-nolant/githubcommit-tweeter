from twitter import *
# personal information
consumer_key = 'abc'
secret = 'abc'
token = 'abc'
token_secret = 'abc'



def send_tweet(quote: str):
    t = Twitter(
        auth=OAuth(token, token_secret, consumer_key, secret))
    # Authentication of access token and secret
    t.statuses.update(
        status=str(quote))


