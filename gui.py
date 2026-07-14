import streamlit as st
from backend import get_news

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

PAGE_SIZE = 50

if "visible_count" not in st.session_state:
    st.session_state.visible_count = PAGE_SIZE

data_load_state = st.text('☢ Loading data...')
data = get_news()
data_load_state.empty()

if not data:
    st.info("Can not find news!")
else:
    st.markdown(
        f"<p style='text-align:center; color:#9aa0a6; margin-bottom:1.2rem;'>"
        f"✔ {len(data)} relevant articles found across your interests - prooooooooooooba</p>",
        unsafe_allow_html=True,
    )

    visible = data[: st.session_state.visible_count]

    for article in visible:
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
                f"<p style='color: #f9fcfb; font-size: 0.85rem; font-weight: 600;'>"
                f"🌐 {article['source']} • 📅 {article['date']} • 🏷️ {article.get('category', 'general')}</p>",
                unsafe_allow_html=True)

            if article["description"]:
                st.markdown(f"<p style='color: #f9fcfb; font-size: 0.95rem;'>{article['description']}</p>",
                            unsafe_allow_html=True)

            st.link_button("Read more ↗️", article["link"], use_container_width=True)

        st.write("")

    if st.session_state.visible_count < len(data):
        if st.button("⬇️ Load more", use_container_width=True):
            st.session_state.visible_count += PAGE_SIZE
            st.rerun()
    else:
        st.caption("That's all for today — check back tomorrow for more.")