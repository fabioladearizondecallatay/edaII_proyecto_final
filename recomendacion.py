import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Función para crear recomendaciones
def recommend_movies(movie_title, movies, n=5):
    """
    Genera recomendaciones de películas basadas en el título dado.
    """
    # Validar título
    if movie_title not in movies["title"].values:
        print(f"'{movie_title}' no encontrado en la base de datos.")
        return {}

    # Combinar géneros como texto
    movies["combined"] = movies["title"] + " " + movies["genres"]

    # Crear matriz de características con CountVectorizer
    count_vectorizer = CountVectorizer(stop_words='english')
    count_matrix = count_vectorizer.fit_transform(movies["combined"])

    # Calcular similitud coseno
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    # Buscar índice de la película base
    idx = movies[movies["title"] == movie_title].index[0]

    # Obtener las puntuaciones de similitud para la película base
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Ordenar las películas por similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Seleccionar las películas más similares
    sim_scores = sim_scores[1:n+1]

    # Obtener los títulos de las películas recomendadas
    recommended_movies = {movies.iloc[i[0]]["title"]: i[1] for i in sim_scores}

    return recommended_movies
