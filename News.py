import feedparser
from textblob import TextBlob

rss_url = "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms"
feed = feedparser.parse(rss_url)

positive_news = []
negative_news = []
neutral_news = []

for entry in feed.entries:
    title = entry.title
    description = entry.description
    
    analysis = TextBlob(title)
    sentiment = analysis.sentiment.polarity

    if sentiment > 0:
        positive_news.append(title)
    elif sentiment < 0:
        negative_news.append(title)
    else:
        neutral_news.append(title)

print("Positive News:")
for news in positive_news:
    print(f"- {news}")

print("\nNegative News:")
for news in negative_news:
    print(f"- {news}")

print("\nNeutral News:")
for news in neutral_news:
    print(f"- {news}")
