## Twitter Purger
a simple twitter script that blocks every private account that lurks in your profile without you following them, no graphical interface but the user experince is not that hard to follow  
# If you're looking for a download link to just use the script here it is: [Download](https://mohanedattef.github.io/Twitter-Purge/purge.exe)  
It'll open a link and once you authoraize it you provide the script with the pin, if later i turn this into a web application this step won't be needed.  
also I know the list of authoraizations you need to provide is a lot but this is the level of authorization that needs to happen to block someone.  
# Requirements 
You'll need nothing to excute the downloadable script above but if you wanna tinker with the code you'll obviously need twitter api credentials that you'll add in the **.env** file and you'll also need to have the **tweepy** library installed, the rest of the imports come with python.

# Files
**purge.py** Simply executes the purge with no interface provided, granted you've provided it with all of your api keys and access tokens.  
**purgeauth.py** Is the file that was packaged that you might install to use it, it implements the  3-Legged OAuth to allow all users to use the script.   
