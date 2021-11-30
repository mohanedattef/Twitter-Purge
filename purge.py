import tweepy
from dotenv import load_dotenv
import os
import time


def apiAuthenticaion():
    load_dotenv()
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    ACCESS_SECRET = os.getenv('ACCESS_SECRET')
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


def getfollowers(api):
    followers = []
    for page in tweepy.Cursor(api.get_followers,count=200).pages():
        try:
            followers.extend(page)
        except tweepy.TweepError as e:
            print("Going to sleep:", e)
            time.sleep(60)
    return followers


def getfriends(api):
    friends=[]
    for page in tweepy.Cursor(api.get_friends,count=200).pages():
        try:
            friends.extend(page)
        except tweepy.TweepError as e:
            print('zeby',e)
            time.sleep(60)
    return friends

def run():
    api=apiAuthenticaion()
    followers=getfollowers(api)
    friends=getfriends(api)
    for follower in followers:
        if(follower.protected and follower not in friends):
            print (follower.screen_name,'https://twitter.com/'+follower.screen_name)
            api.create_block(user_id=follower.id)
            print("blocked user: "+ follower.screen_name)
        

if __name__ == '__main__':
    run()