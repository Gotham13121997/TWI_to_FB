"""
Created by Gotham on 10-06-2018.
"""
import FacebookWallPoster
import TweetsFetcher
import json
import os
import shutil
from apscheduler.schedulers.background import BackgroundScheduler
from configparser import ConfigParser


def main():
    config = ConfigParser()
    config.read('config.ini')
    scheduler = BackgroundScheduler()
    mount_point = config.get('OPEN SHIFT', 'persistent_mount_point')
    fb_page_access_token = config.get('FACEBOOK', 'page_access_token')
    tw_consumer_key = config.get('TWITTER', 'consumer_key')
    tw_consumer_secret = config.get('TWITTER', 'consumer_secret')
    tw_access_key = config.get('TWITTER', 'access_key')
    tw_access_secret = config.get('TWITTER', 'access_secret')
    tw_handle = config.get('TWITTER', 'handle')

    if not os.path.exists(mount_point + 'db.json'):
        shutil.copy('db.json', mount_point + 'db.json')

    fb_wall_poster = FacebookWallPoster.FacebookWallPoster(fb_page_access_token)
    tweets_fetcher = TweetsFetcher.TweetsFetcher(consumer_key=tw_consumer_key, consumer_secret=tw_consumer_secret,
                                                 access_key=tw_access_key, access_secret=tw_access_secret,
                                                 file_path=mount_point + 'db.json')
    with open(mount_point+'db.json', 'r') as db_read:
        data_list = json.load(db_read)

    @scheduler.scheduled_job('cron', hour='4', minute='30')  # change according to need
    def poster():
        oldest_data = data_list.pop()
        fb_wall_poster.post_to_wall(**oldest_data)
        with open(mount_point + 'db.json', 'w') as db_write:
            json.dump(data_list, db_write)

    @scheduler.scheduled_job('cron', day_of_week='sun')  # change according to need
    def replenish_db():
        tweets_fetcher.store_data(handle=tw_handle)

    scheduler.start()


if __name__ == '__main__':
    main()
    # infinite loop to keep the script always running
    while True:
        pass

