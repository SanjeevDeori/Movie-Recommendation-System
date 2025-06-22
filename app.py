import streamlit as st
import pandas as pd
import requests
import pickle
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv('TMDB_API_KEY')

if not API_KEY:
    st.error("TMDB API key not found. Please add it to your .env or Streamlit secrets.")
    st.stop()

# Efficient loading of data using Streamlit resource caching
@st.cache_resource
def load_data():
    try:
        with open('movie_data.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error("movie_data.pkl not found. Ensure it's in your repo.")
        st.stop()

movies, cosine_sim = load_data()

# Cache API calls per poster
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"https://image.tmdb.org/t/p/w185{data.get('poster_path')}"
    return "https://via.placeholder.com/185x278.png?text=No+Image"

def get_recommendations(title):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sim_scores]
    titles = movies.iloc[movie_indices]['title'].values
    ids = movies.iloc[movie_indices]['id'].values
    posters = [fetch_poster(movie_id) for movie_id in ids]
    return titles, posters

# Streamlit UI layout
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

st.markdown("""
    <div style='text-align: center; padding-bottom: 5px;'>
        <h1 style='margin-bottom: 2px;'>🎬 Movie Recommendation System</h1>
        <p style='font-size: 16px; color: grey; margin-top:0;'>Get suggestions based on your favorite movie</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    selected_movie = st.selectbox("Choose a movie", movies['title'].values, label_visibility="collapsed")
    if st.button("🍿 Recommend"):
        titles, posters = get_recommendations(selected_movie)

        for row in range(2):
            cols = st.columns(5)
            for i in range(5):
                idx = row * 5 + i
                with cols[i]:
                    st.image(posters[idx], width=160)
                    st.caption(titles[idx])
            if row == 0:
                st.markdown("<div style='margin-bottom: -25px;'></div>", unsafe_allow_html=True)
