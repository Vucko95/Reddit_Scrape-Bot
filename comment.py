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
word = 'honest'
posts_last_24h = []
for post in subreddit.new():
    current_time = datetime.utcnow()
    post_time = datetime.utcfromtimestamp(post.created)
    deltatime = current_time - post_time
    if deltatime <= timedelta(hours=24):
        if "honest" in post.title.lower():
            print(post.title)
            print("Word is there")
            post.reply('Chiristmas is there')
        # for comment in post.comments:
        #     if "honest" in comment.body.lower():
        #         comment.reply("Commented")
