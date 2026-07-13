import requests
from datetime import date, timedelta, datetime
import os
from dotenv import load_dotenv
from datetime import date, timedelta
from newsapi.newsapi_client import NewsApiClient
import streamlit as st

load_dotenv()
api_key = os.getenv("API_KEY")
INTERESTS = '(AI OR "artificial intelligence" OR "machine learning" OR "generative AI" OR LLM OR cybersecurity OR "cyber security" OR cyberattack OR "data breach" OR ransomware OR malware OR hacking OR phishing OR vulnerability OR "video games" OR gaming OR "game development" OR hardware OR "graphics card" OR GPU OR CPU OR "PC components" OR "tech industry" OR IT OR "new movies" OR "movie releases" OR "upcoming films" OR actors OR "actor interviews" OR "celebrity interviews" OR "good music" OR "music releases" OR "new album")'
# initializare client
newsapi = NewsApiClient(api_key=api_key)

@st.cache_data
def get_news():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    today = date.today().isoformat()

    query = INTERESTS
    try:
        response = newsapi.get_everything(
            q=query,
            from_param=yesterday,
            to=today,
            language='en',
            sort_by='relevancy',
            page_size=50,
            page=1
        )

        formatted_articles = []
        for article in response.get('articles', []):
            if article['title'] == "[Removed]" or not article['title']:
                continue

            formatted_articles.append({
                "image": article.get('urlToImage'),
                "title": article['title'],
                "source": article['source']['name'],
                "date": article['publishedAt'][:10],
                "description": article.get('description', ''),
                "link": article['url']
            })

        return formatted_articles
    except Exception as e:
        st.error(f"ERROR API: {e}")
        return []