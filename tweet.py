import tweepy
import os

from get_planet_stats import get_planet_stats

def format_number(number):
    return f"{int(number):,}"

schedule = os.environ.get("SCHEDULE")

TWEET_TITLE = {
    "Day": "OSM Daily Stats 📊",
    "Week": "OSM Weekly Stats 📊",
    "Month": "OSM Monthly Stats 📊"
}

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

report_run_at, report, number_of_editors, top_users = get_planet_stats()
top_users = top_users[schedule]


if __name__ == "__main__":
    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )

    tweet_text = (
        f"{TWEET_TITLE[schedule]}\n\n"
        f"Users: {format_number(report['Number of users'])} 👥\n\n"
        "Users that...\n"
        f"edited nodes: {format_number(number_of_editors[1][schedule])} ✏️\n"
        f"uploaded GPX: {format_number(number_of_editors[0][schedule])} 🗺️\n\n"
        "Top 3 editors:\n"
        f"1. {top_users[0][1]} - {format_number(top_users[0][0])} 🥇\n"
        f"2. {top_users[1][1]} - {format_number(top_users[1][0])} 🥈\n"
        f"3. {top_users[2][1]} - {format_number(top_users[2][0])} 🥉\n\n"

        f"{report_run_at}\n\n"
        
        "#OpenStreetMap #OSM #OSMstats"
    )

    response = client.create_tweet(text=tweet_text)

    print(tweet_text)
    print(len(tweet_text))