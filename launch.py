import github_find
import time
import tweet_send
import os

def restart():
    print("Restarting...")
    os.system("python launch.py")
    quit()

while 1:
    tweet = github_find.begin()
    print(tweet, " : sent")

    response = tweet_send.send_tweet(tweet)
    if response == 1:
        print("Complete. Waiting 1 hour before next post.")
        time.sleep(3600)
        restart()
    else:
        restart()
