import webapp2
import ConfigParser
import tweepy

config = ConfigParser.RawConfigParser()
config.read('settings.cfg')

consumer_key = config.get("Twitter API", "CONSUMER_KEY")
consumer_secret = config.get("Twitter API", "CONSUMER_SECRET")
access_token_key = config.get("Twitter API", "ACCESS_TOKEN_KEY")
access_token_secret = config.get("Twitter API", "ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

keyword = "fart"
phrase = "FARTBOT APPROVES."

class MainHandler(webapp2.RequestHandler):
    def get(self):
        results = api.search(q="fart", lang="en")

        for Status in results:
            if "RT" not in Status.text and keyword not in Status.user.screen_name.lower() and keyword not in Status.user.name.lower():
                api.update_status(phrase + " " + "https://twitter.com/" + Status.user.screen_name + "/status/" + Status.id_str)
                break

app = webapp2.WSGIApplication([
    ('/activate_fartbot', MainHandler)
], debug=True)
