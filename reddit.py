import praw
import prawcore

try: 
    reddit = praw.Reddit('bot1', user_agent='cpqp user agent')

    print(reddit.read_only)
    
    subreddit = reddit.subreddit('Python')

    # hot_python = subreddit.hot(limit=15)

    # for submission in hot_python: 
    #     if not submission.stickied:
    #         print(submission.title)
    #         print(submission.score)
    #         print(submission.id)
    #         print(submission.url)
    #         print('\n\n')
            
except prawcore.exceptions.ResponseException as e:
    print e
    
    