FROM python:3.9

ADD fetch_tweets.py .

ADD twitter_keys.py .

RUN pip install pandas tweepy datetime

CMD [ "python", "./fetch_tweets.py" ]