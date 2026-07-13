import requests
from datetime import date, timedelta
import os
from dotenv import load_dotenv
from datetime import date, timedelta
from newsapi.newsapi_client import NewsApiClient

load_dotenv()
api_key = os.getenv("API_KEY")

yesterday = (date.today() - timedelta(days=1)).isoformat()
today = date.today()

# initializare client
newsapi = NewsApiClient(api_key=api_key)


query = '(AI OR "artificial intelligence" OR "machine learning" OR "generative AI" OR LLM) AND (cybersecurity OR "cyber security" OR cyberattack OR "data breach" OR ransomware OR malware OR hacking OR phishing OR vulnerability)'
response = newsapi.get_everything(
    q=query,
    from_param=yesterday,
    to=today,
    language='en',
    sort_by='relevancy',
    page_size=100,
    page=1
)

total_news = response['totalResults']

for article in response['articles']:
    image = article['urlToImage']
    title = f"📰 {article['title']}"
    source = f"🌐 {article['source']['name']}"
    date_posted = f"📅 {article['publishedAt']}"
    link = f"{article['url']}"
    print (title)