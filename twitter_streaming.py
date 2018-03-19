#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "74730475-VxeKDIYrhpIhGDTnbfTgysAmoDiYNomRzaobz58sf"
access_token_secret = "7KAKplYbsk8ILJ8lDxoKXm4xww1lsCbHBY3sGQyAElp5A"
consumer_key = "GIPDGDwmwpAYsFLhExnNoirpt"
consumer_secret = "7w68GkbleouLu46BvogonL945LYS3msJ3BvfekveLeDNyNPlGK"


#This is a basic listener that just prints received tweets to stdout.


# This listener will print out all Tweets it receives
class PrintListener(StreamListener):
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)

        # Print out the Tweet
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()

    # Show system message
    print('I will now print Tweets containing "Python"! ==>')

    # Authenticate
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to our listener
    stream = Stream(auth, listener)
    stream.filter(track=['Python'])