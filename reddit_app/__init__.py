import ConfigParser

import praw


def main():

    parser = ConfigParser.ConfigParser()
    parser.read('reddit_app.cfg')
    reddit = praw.Reddit(client_id=parser.get('reddit', 'client_id'),
                         client_secret=parser.get('reddit', 'client_secret'),
                         password=parser.get('reddit', 'password'),
                         user_agent=parser.get('reddit', 'user_agent'),
                         username=parser.get('reddit', 'username'))
    print("User: {}".format(reddit.user.me()))

    print('Done')

if __name__ == '__main__':
    main()