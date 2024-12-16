from data import load_and_process_data, assign_images
from recomendacion import recommend_movies
from grafica_interactiva import create_graph_and_list
import pandas as pd

def main():
    #Paso 1: Cargar las películas y seleccionar cuántas mostrar
    num_movies = int(input("\nIngrese el número de películas que desea ver en la base de datos: "))
    min_rating = float(input("\nIngrese el rating mínimo que deben tener las películas: "))
    
    movies, ratings = load_and_process_data()

    #Filtrar las películas por el rating mínimo
    if "rating" in movies.columns:
        movies = movies[movies["rating"] >= min_rating]

    #Muestreo aleatorio para evitar sesgo por orden
    movies = movies.sample(n=num_movies, random_state=42) if len(movies) > num_movies else movies

    #Reiniciar los índices después del muestreo
    movies = movies.reset_index(drop=True)

    #Asignar imágenes a las películas seleccionadas
    movies = assign_images(movies)

    # Mostrar las películas seleccionadas
    print("Películas seleccionadas:")
    if "year" in movies.columns:
        print(movies[["title", "year", "rating"]].to_string(index=False))
    else:
        print(movies[["title", "rating"]].to_string(index=False))

    # Paso 2: Obtener recomendaciones
    movie_title = input("Ingrese el título de una película para recibir recomendaciones: ")
    recommendations = recommend_movies(movie_title, movies)

    # Paso 3: Crear gráfica interactiva
    if recommendations:
        create_graph_and_list(movie_title, recommendations, movies)

if __name__ == "__main__":
    main()