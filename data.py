import pandas as pd
import requests
import os

# Clave de API de TMDb
API_KEY = "e59c32127d83a5a69a297182f09f6661"  # Reemplázalo con tu clave real
BASE_URL = "https://api.themoviedb.org/3"

# Funciones para obtener imágenes desde la API
def get_movie_image(title):
    #Obtiene la URL de la imagen de una película dado su título.
    clean_title = title.split(" (")[0]  # Ejemplo: "Toy Story (1995)" -> "Toy Story"
    
    params = {
        "api_key": API_KEY,
        "query": clean_title
    }
    
    response = requests.get(f"{BASE_URL}/search/movie", params=params)
    if response.status_code == 200 and response.json()["results"]:
        return f"https://image.tmdb.org/t/p/w500{response.json()['results'][0]['poster_path']}"
    return None

def assign_images(movies):
    
    #Asigna URLs de imágenes a las películas.
    movies["image"] = movies["title"].apply(get_movie_image)
    return movies

def load_and_process_data():
    
    #Carga y procesa la base de datos de películas.
    movies = pd.read_csv("movies.csv")
    if "ratings.csv" in os.listdir():
        ratings = pd.read_csv("ratings.csv")
        # Calcular rating promedio por película si los ratings existen
        avg_ratings = ratings.groupby("movieId")["rating"].mean().reset_index()
        movies = movies.merge(avg_ratings, on="movieId", how="left")
    else:
        ratings = None
    return movies, ratings