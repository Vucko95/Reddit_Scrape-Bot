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
subreddit = reddit.subreddit("pythonsandlot")
# subreddit.validate_on_submit = True
title = 'This is a Test'
content = """
Hello, Just testing python Script
"""
subreddit.submit(title=title, selftext=content)
