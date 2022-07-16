from dotenv import load_dotenv
import os
import praw
load_dotenv()
user_id = os.environ.get('id')
secret = os.environ.get('secret')
pw = os.environ.get('pw')

reddit = praw.Reddit(user_agent=True, client_id=f"{user_id}",
                     client_secret=f"{secret}", username='Python_automation666', password=f"{pw}")

url = "https://www.reddit.com/r/notinteresting/comments/w08ndb/name_something_less_interesting_than_a_brick/"
post = reddit.submission(url=url)
# print(post.title)
# print(post.selftext)
# Printing comments
for comment in post.comments:
    print(comment.body)
