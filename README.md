# CurioStream 
### *Smart News Aggregator for domains I am interested in*

---

## Project Description
A sleek, lightweight web application built with Streamlit and NewsAPI that aggregates and displays the most popular news from the past 24 hours based on a highly customized set of personal interests.

## Features

* **Tailored Feed:** Automatically queries news matching a precise boolean logic search covering keywords about domains I am interested in eg: video games, AI etc.
* **Performance Optimization:** Utilizes Streamlit's `@st.cache_data` caching mechanism to prevent redundant API calls and speed up load times.
* **Modern UI:** A clean, centered dark-mode dashboard featuring responsive news cards, fallback images for missing visual data, and direct outbound links to source articles.
* **Data Cleaning:** Automatically filters out broken or placeholder data (such as articles flagged as `[Removed]`) returned by the API provider.

## Setup and Installation

### 1. Ensure you have Python 3.8+ installed on your system. You will also need a free API key from NewsAPI.org.
### 2. Clone this repository
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Environment configuration
Create a .env file in the root directory of the project to securely store your API key:
```bash
API_KEY=your_actual_newsapi_key_here
```
