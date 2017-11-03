import ConfigParser
import json

import praw


def main():

    parser = ConfigParser.ConfigParser()
    parser.read('reddit_app.default.cfg')
    parser.read('reddit_app.cfg')
    reddit = praw.Reddit(client_id=parser.get('reddit', 'client_id'),
                         client_secret=parser.get('reddit', 'client_secret'),
                         password=parser.get('reddit', 'password'),
                         user_agent=parser.get('reddit', 'user_agent'),
                         username=parser.get('reddit', 'username'))

    print("User: {}".format(reddit.user.me()))

    subreddit = reddit.subreddit('sneakerstestcss')
    posts = []
    for submission in subreddit.search('flair:"contest"', limit=10):
        submission_json = {}
        submission_json['title'] = submission.title
        submission_json['url'] = submission.url
        submission_json['author'] = submission.author.name
        posts.append(submission_json)

    with open('test.json', 'w+') as f:
        json.dump(posts, f)

if __name__ == '__main__':
    main()