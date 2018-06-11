"""
Created by Gotham on 11-06-2018.
"""
import tweepy
import json


class TweetsFetcher:
    def __init__(self, consumer_key, consumer_secret, access_key, access_secret, file_path):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth)
        self.file_path = file_path

    def get_new_tweets(self, screen_name, since_id):
        """
        :param screen_name: handle
        :param since_id: last id of tweet after which you want to fetch tweets from
        :return: tweets object 
        """
        # here max count possible is 200
        if since_id is not None:
            return self.api.user_timeline(screen_name=screen_name, since_id=since_id, count=200)
        else:
            return self.api.user_timeline(screen_name=screen_name, count=200)

    def save_data(self, handle, since_id):
        new_tweets = self.get_new_tweets(handle, since_id)
        data_dict_list = []
        for tweet in new_tweets:
            try:
                data_dict = {}
                tweet_dict = tweet._json # this is the tweet in dictionary form
                """
                You can use other keys from tweet here only three are used
                """
                data_dict['link'] = tweet_dict['entities']['urls'][0]['expanded_url']
                data_dict['id'] = tweet_dict['id_str']
                data_dict['message'] = tweet_dict['text']
                data_dict_list.append(data_dict)
            except:
                pass
        return data_dict_list

    def store_data(self, handle):
        with open(self.file_path, mode='r', encoding='utf-8') as db:
            data = json.load(db)
        # checking if we already have tweets in db
        if len(data) == 0:
            # if no
            data = self.save_data(handle=handle, since_id=None)
        else:
            # else add new tweets along with old ones
            data_new = self.save_data(handle=handle, since_id=data[0]["id"])
            data_new.extend(data)
            data = data_new
        with open(self.file_path, mode='w', encoding='utf-8') as db:
            json.dump(data, db)
