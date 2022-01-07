import github_find, time
import tweet_send
i = 1
while i:
    tweet = github_find.begin()
    print(tweet, " : sent")
    
    print("Complete. Waiting 1 hour before next post.")
    tweet_send.send_tweet(tweet)
    time.sleep(3600)
    