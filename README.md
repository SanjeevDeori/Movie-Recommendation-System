# 🎬 Movie Recommendation System

A **Streamlit web application** 🌐 that recommends similar movies based on your favourite selected movies using **content-based filtering** powered by **cosine similarity**. It uses a preprocessed TMDB dataset and fetches real-time movie posters from the **TMDB API** to enhance user experience.
---

## ✨ Features

✅ Select a movie and get **top 10 similar movie recommendations**  
✅ Uses **content-based filtering** via TF-IDF and cosine similarity  
✅ Fetches and displays movie **posters** using the TMDB API  
✅ Fast, responsive, and **interactive UI with Streamlit**  
✅ Built-in **caching** to avoid recomputing on repeated inputs  
✅ Clean and modular code structure for easy updates  
✅ **Scalable** to integrate collaborative filtering or hybrid models

---
## 🚀 Live Demo

Deployed at Streamlit.app:

👉 **[movie-recommender-san.streamlit.app](https://movie-recommender-san.streamlit.app)**

## 🧰 Technologies Used

- 🐍 Python  
- 🎈 Streamlit  
- 📊 scikit-learn  
- 🗃 pandas, numpy  
- 🖼 TMDB API  
- 🧠 Cosine Similarity (ML-based filtering)

---

## ⚙️ Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/SanjeevDeori/Movie-Recommendation-System.git
   cd Movie-Recommendation-System
   ```
2. Install dependencies:
   ```bash
     pip install -r requirements.txt
   ```
3. Add your TMDB API key to .env:
   ```bash
     env
     TMDB_API_KEY=your_tmdb_api_key_here
   ```

## 🚀 Usage
Run the Streamlit app locally by executing:

```bash
streamlit run app.py
```
- Select a movie title from the dropdown.

- Click Recommend to get the top 10 similar movies.

- The app will display the movie titles along with their posters.

## Results

The system provides the top 10 recommended movies for any selected movie title. It also fetches and displays the posters of these recommended movies using the TMDB API.

![Screenshot 2025-06-22 120116](https://github.com/user-attachments/assets/ad082d15-bf73-4e92-837c-e78374975028)

## 📊 Dataset
- 📁 Source: [TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)



## 📄 License
This project is licensed under the MIT License.

## 📬 Contact
For questions, suggestions, or collaboration:
- GitHub: @SanjeevDeori

- Email: sanjeevdeori743.jams@gmail.com

Happy Watching! 🎥🍿
