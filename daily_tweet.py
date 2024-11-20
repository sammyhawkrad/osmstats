import tweepy
import os

from get_planet_stats import get_planet_stats

def format_number(number):
    return f"{int(number):,}"

report_run_at, report, number_of_editors, top_users = get_planet_stats()
top_users = top_users['Day']

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

if __name__ == "__main__":
    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )

    tweet_text = f"""
    OSM Daily Stats 📊
    
    Users: {format_number(report['Number of users'])} 👥

    Users that...
    edited nodes: {format_number(number_of_editors[1]['Day'])} ✏️
    uploaded GPX: {format_number(number_of_editors[0]['Day'])} 🗺️

    Top 3 editors:
    1. {top_users[0][1]} - {format_number(top_users[0][0])} 🥇
    2. {top_users[1][1]} - {format_number(top_users[1][0])} 🥈
    3. {top_users[2][1]} - {format_number(top_users[2][0])} 🥉

    #OpenStreetMap #OSM #OSMstats
    """

    response = client.create_tweet(text=tweet_text)

    print(response)
    print(len(tweet_text))