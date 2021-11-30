import tweepy
from dotenv import load_dotenv
import os
import time
import webbrowser

def apiAuthenticaion():
    load_dotenv()
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    try:
        redirect_url = auth.get_authorization_url()
        webbrowser.open(redirect_url)
        print("Open this link to authorize the script: "+redirect_url)
        verifier = input('enter the PIN your just received: ').strip()
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
    
    auth.get_access_token(verifier)
    auth.set_access_token(auth.access_token, auth.access_token_secret)
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
            print('Going to sleep:',e)
            time.sleep(60)
    return friends


def run():
    api=apiAuthenticaion()
    print("authentication successful!")
    followers=getfollowers(api)
    print("fetched your list of followers")
    friends=getfriends(api)
    print("fetched your list of friends")
    enemiesofthestate=[]
    for follower in followers:
        if(follower.protected and follower not in friends):
            enemiesofthestate.append(follower)
    print("fetched your lurkers \n")
    while True:
        decision=input('Would you like to block everyone or pick your fighters? Enter e for everyone, f for fighters, l to view all your lurkers and enter x to exit.\n')
        if decision =='e':
            confirm=input('Are you sure you want to block everyone? this action is irrevirsable, press e to confirm, x to exit.\n')
            if confirm == 'e':
                for enemy in enemiesofthestate:
                    api.create_block(user_id=enemy.id)
                    print("blocked user: "+ enemy.screen_name)
            elif confirm == 'x':
                exit()
            else:
                print("that wasn't a correct input, try again")
        elif decision == 'f':
            for enemy in enemiesofthestate:
                while True:
                    print ("Would you like to block: "+enemy.screen_name +' https://twitter.com/'+enemy.screen_name+ "\n")
                    block=input("y/n: ")
                    if block == 'y':
                        api.create_block(user_id=enemy.id)
                        print("Blocked user: "+ enemy.screen_name)
                        break
                    elif block == 'n':
                        break
                    elif block =='x':
                        break
                    else:
                        print('Wrong input')
                        continue
        elif decision== 'l':
            for enemy in enemiesofthestate:
                print(enemy.screen_name+' https://twitter.com/'+enemy.screen_name+ "\n")
            print("You have a total of {} lurkes \n".format(len(enemiesofthestate)))
        elif decision == 'x':
            exit()
        else:
            print("That wasn't a correct input, try again")
            continue
    
            
if __name__ == '__main__':
    run()