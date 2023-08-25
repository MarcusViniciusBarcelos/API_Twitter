# src/services.py
import tweepy
from src.constants import *
from src.secrets import *
from src.connection import trends_collection


class TwitterService:
    def __init__(self):
        auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        self.api = tweepy.API(auth)

    def save_global_trends_to_mongo(self):
        global_trends = self._get_global_trends()

        for trend in global_trends:
            trends_collection.insert_one({"name": trend})

    def get_global_trends(self):
        return self._get_global_trends()

    def _get_global_trends(self):
        response = self.api.get_place_trends(id=WORLDWIDE_WOE_ID, lang="en")
        trends = []

        if "data" in response:
            trends = [trend["name"] for trend in response["data"][0]["trends"]]

        return trends

