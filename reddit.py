import praw
import prawcore

try: 
    reddit = praw.Reddit('bot1', user_agent='cpqp user agent')

    subreddit = reddit.subreddit('WorldNews')
                            
    hot_submissions = subreddit.hot(limit=10)
    
    for submission in hot_submissions: 
        if ("trump" in submission.title.lower()):
            print(submission.title)
            print(submission.score)
            print("\n\n")
            
except prawcore.exceptions.ResponseException as e:
    print e
    