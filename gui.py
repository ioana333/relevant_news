import streamlit as st
from main import get_news

st.set_page_config(page_title="News", page_icon="📰", layout="centered")

st.markdown("<h1 style='text-align: center; color: #f9fcfb;'>📰Yesterday's news</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117; 
    }
    </style>
    """,
    unsafe_allow_html=True
            )

data_load_state = st.text('☢ Loading data...')
data = get_news()
data_load_state.text('✔ These are relevant news for you')

if not data:
    st.info("Can not find news!")
else:
    for article in data:
        with st.container(border=True):
            if article["image"]:
                st.image(article["image"], use_container_width=True)
            else:
                st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=800&auto=format&fit=crop",
                         use_container_width=True)
            st.markdown(
                f"<h3 style='font-size: 1.25rem; font-weight: bold; margin-top: 8px; color: #f9fcfb;'>{article['title']}</h3>",
                unsafe_allow_html=True)

            st.markdown(
                f"<p style='color: #f9fcfb; font-size: 0.85rem; font-weight: 600;'>🌐 {article['source']} • 📅 {article['date']}</p>",
                unsafe_allow_html=True)

            if article["description"]:
                st.markdown(f"<p style='color: #f9fcfb; font-size: 0.95rem;'>{article['description']}</p>",
                            unsafe_allow_html=True)

            st.link_button("Reed more ↗️", article["link"], use_container_width=True)

        st.write("")
