import requests
from datetime import date, timedelta, datetime
import os
from dotenv import load_dotenv
from datetime import date, timedelta
from newsapi.newsapi_client import NewsApiClient
import streamlit as st
from numpy.random import shuffle

from interests import CATEGORIES

load_dotenv()
api_key = os.getenv("API_KEY")

# initializare client
newsapi = NewsApiClient(api_key=api_key)

@st.cache_data(ttl=3600 * 6)
def get_news():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    today = date.today().isoformat()

    category_news = []
    seen_urls = []

    for label, query in CATEGORIES.items():

        try:
            response = newsapi.get_everything(
                q=query,
                from_param=yesterday,
                to=today,
                language='en',
                sort_by='relevancy',
                page_size=100,
                page=1
            )
        except Exception as e:
            st.error(f"ERROR API: {e}")
            continue

        formatted_articles = []
        for article in response.get('articles', []):
            if article['title'] == "[Removed]" or not article['title']:
                continue
            if article['url'] in seen_urls:
                continue

            seen_urls.append(article['url'])
            formatted_articles.append({
                "image": article.get('urlToImage'),
                "title": article['title'],
                "source": article['source']['name'],
                "date": article['publishedAt'][:10],
                "description": article.get('description', ''),
                "link": article['url'],
                "category": label
            })

        category_news.append(formatted_articles)
    all_news = shuffle_custom(category_news)
    return all_news



def shuffle_custom(category_news):
    result = []
    max_len = max((len(cat) for cat in category_news), default=0)

    for i in range(max_len):
        round_batch = [cat[i] for cat in category_news if i < len(cat)]
        shuffle(round_batch)
        result.extend(round_batch)
    return result