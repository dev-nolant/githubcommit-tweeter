import github_find
import time
import os

def restart():
    print("Restarting...")
    os.system("python launch.py")
    quit()

while 1:
    tweet = github_find.begin()
    github_find.send_tweet(tweet)
    print(tweet, " : sent")
    print("--------------------------------")
    print("Complete. Waiting 1 hour before next post.")
    time.sleep(3600)
    restart()
    