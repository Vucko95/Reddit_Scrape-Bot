from datetime import date, datetime, timedelta
from dotenv import load_dotenv
import os
from datetime import datetime
from flask import current_app
import praw
load_dotenv()
user_id = os.environ.get('id')
secret = os.environ.get('secret')
pw = os.environ.get('pw')

reddit = praw.Reddit(user_agent=True, client_id=f"{user_id}",
                     client_secret=f"{secret}", username='Python_automation666', password=f"{pw}")
subreddit = reddit.subreddit("FriedChicken")
posts24h = []
with open('output.txt', 'w') as file:
    for post in subreddit.new():
        current_time = datetime.utcnow()
        post_time = datetime.utcfromtimestamp(post.created)
        deltatime = current_time - post_time
        # print(deltatime)
        if deltatime <= timedelta(hours=24):
            # print(post.title)
            # print(post.title, post.selftext)
            posts24h.append((post.title, post.selftext))
            file.write(f'{post.title}\n{post.selftext}\n\n')

# print(posts24h)
