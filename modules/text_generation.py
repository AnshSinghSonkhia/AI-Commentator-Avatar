# modules/text_generation.py

from GoogleNews import GoogleNews
from newspaper import Article
from urllib.parse import urlparse, urlunparse
import logging
import re

logging.basicConfig(level=logging.ERROR)

def clean_url(url):
    # Remove any tracking/query strings like &ved=... or ?utm=...
    url = re.split(r"[&?]", url)[0]

    # Parse and reconstruct the URL
    parsed = urlparse(url)
    cleaned = parsed._replace(
        path=parsed.path.lower().rstrip("/"),  # lowercase the path, remove trailing slash
        query='', fragment=''
    )
    return urlunparse(cleaned)

def fetch_latest_news_with_content(topic="India", count=3):
    print(f"\n🔍 Top {count} Latest News on: {topic}\n")
    googlenews = GoogleNews(lang='en', region='IN')
    googlenews.search(topic)
    news = googlenews.results(sort=True)[:count]

    final_combined_content = ""

    for item in news:
        title = item.get('title', 'No Title')
        raw_link = item.get('link', '')
        clean_link = clean_url(raw_link)

        print(f"📰 {title}")
        print(f"🔗 {clean_link}\n")

        try:
            article = Article(clean_link, language="en")
            article.download()
            article.parse()
            content = article.text.strip()

            if content:
                print("📝 Content:")
                print(content[:500] + "...\n")  # Show content preview
                final_combined_content += content + "\n\n"
            else:
                print("⚠️ Content not found.\n")
        except Exception as e:
            logging.error(f"❌ Error fetching article content from {clean_link}: {e}")
            print("⚠️ Failed to extract article content.\n")

        print("=" * 100)

    return final_combined_content.strip()




