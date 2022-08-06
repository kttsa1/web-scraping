import praw

reddit = praw.Reddit(client_id='-v1GeBEDL0aPvVu6wahwfA', client_secret='LNUeU3rPUlho8HA_V7QOu-RuPQSFMA', user_agent='WebScraping')
hot_posts = reddit.subreddit('UVA').hot(limit=10)

for post in hot_posts:
    print(post.title)