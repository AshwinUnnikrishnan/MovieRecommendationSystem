import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{0}?api_key=14bce81ae42aa0dd79fe23bcf9474a9a&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] # fetches index in the main list of the movie
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for mov in movies_list:
        recommended_movies.append(movies.iloc[mov[0]].title)

        recommended_movies_posters.append(fetch_poster(movies.iloc[mov[0]].movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_Movie_Name = st.selectbox(
    'Please Select or Write the Movie Name',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_Movie_Name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])