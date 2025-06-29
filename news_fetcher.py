import feedparser

def fetch_top_tech_news(feed_url, limit=5):
    feed = feedparser.parse(feed_url)
    top_entries = feed.entries[:limit]
    
    news_items = []
    for entry in top_entries:
        title = entry.title
        summary = entry.summary if hasattr(entry, 'summary') else ''
        news_items.append(f"Title: {title}\nSummary: {summary}\n")

    return "\n".join(news_items)

if __name__ == "__main__":
    url = "https://techcrunch.com/feed/"
    tech_news = fetch_top_tech_news(url)
    print(tech_news)
