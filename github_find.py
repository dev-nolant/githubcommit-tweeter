import os
import random
import time
import tweepy
from github import Github

from timeout import timeout

funny_words = open("swear_words.txt", "r").readlines()

ACCESS_TOKEN = 'abc'#change

g = Github(ACCESS_TOKEN)

TIMEOUT_ = 240

consumer_key = 'abc'#change
secret = 'abc'#change
token = 'abc'#change
token_secret = 'abc'#change

auth = tweepy.OAuthHandler(consumer_key, secret)
auth.set_access_token(token, token_secret)

api = tweepy.API(auth)
tweets = []
for tweet in tweepy.Cursor(api.user_timeline).items():
    tweets.append(tweet.text)


def send_tweet(quote: str):

    api.update_status(str(quote))
    return 1


def random_number(count):
    number = random.randint(1, count)
    return number


def remove_word(word):
    # Read in the file
    with open('swear_words.txt', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(word, '')

    # Write the file out again
    with open('swear_words.txt', 'w') as file:
        file.write(filedata)
        file.close()
    print(f"Removed word: {word}")


# Active timeout. Can be changed with var above
"""[Search GitHub with funny/profanity word]
Search all of GitHub commits for the word, and then parse the commit comments.
Returns:
    [string]: [body of the commit chosen]
"""


@timeout(TIMEOUT_)
def search_github(keyword):
    query = f'"merge: {keyword}'
    results = g.search_commits(query, sort="committer-date", order='desc')
    count = results.totalCount

    if count < 500:
        remove_word(keyword)
        raise Exception('manual fail: search keyword not meeting query')

    print(f'Found {count} commit(s)')

    results = results[random.randint(1, count):]
    filtered = []

    print("Gathering comments...")
    for result in results:
        for comment in result.get_comments():
            comment_content = comment.body
            print(f"COMMENT CHECKED: [{comment_content}]\n-------------")
            if "Successfully deployed" not in comment_content and ".js*" not in comment_content \
                    and comment_content not in tweets and len(comment_content) <= 280:
                if (len(comment_content) > 30):
                    if (keyword not in comment_content):
                        pass
                filtered.append(comment_content)
                return filtered


"""[Start and End of function parsing]
Will start the program, and then if it runs into an error, it will automatically wait 30 secs and restart.

If found correct word, it parses as needed, and executes whatever command you want it to with that string.
"""


def begin():
    try:
        word_used = random.choice(funny_words)
        print(f"Using word: {word_used}")
        results = search_github(word_used)
        return results[0]

    except Exception as e:
        if "second" in str(e):
            print(f"Failed. Waiting 60 secs to restart. ERROR: {str(e)}")
            time.sleep(60)
            print("Restarting...")
            os.system("python launch.py")

        if "search keyword not meeting query" in str(e):
            print("Restarting...")
            os.system("python launch.py")

        if "object is not subscriptable" in str(e):
            remove_word(word_used)

        print(f"Failed. Waiting 30 secs to restart. ERROR: {str(e)}")
        time.sleep(30)
        print("Restarting...")
        os.system("python launch.py")

        exit(0)
