Proyecto : Recomendación de películas

El proyecto es un sistema interactivo de recomendación de películas que combina análisis de datos y visualizaciones para ofrecer recomendaciones personalizadas a los usuarios, basadas en similitudes entre películas. El sistema utiliza un conjunto de datos inicial proveniente de MovieLens, que contiene información sobre 10,000 películas calificadas por 600 personas, generando un total de 100,000 valoraciones. Además, el sistema enriquece esta base de datos con imágenes de los carteles de las películas obtenidas a través de la API de TMDb (The Movie Database), lo que mejora la presentación visual de las recomendaciones.

Funcionamiento del Proyecto

1. Carga y Procesamiento de Datos
En el archivo data.py, se maneja la carga de los datos desde dos archivos CSV: movies.csv y ratings.csv.
El CSV movies.csv contiene títulos y géneros. Si están disponibles, las valoraciones
en ratings.csv se usan para calcular una media de puntuaciones por película. También se conectan con la API de TMDb para asignar imágenes de las películas, que se almacenan en la columna image.

3. Generación de Recomendaciones
El archivo recomendacion.py implementa el motor de recomendación.
Utiliza los géneros y títulos combinados como características textuales para calcular similitudes entre películas con el algoritmo de similitud coseno, implementado mediante los módulos cosine_similarity y CountVectorizer de sklearn.
Este algoritmo mide la similitud entre vectores calculando el coseno del ángulo que forman, donde valores cercanos a 1 indican alta similitud. Los vectores representan palabras clave extraídas de géneros y títulos, y se comparan para generar una lista ordenada de películas similares, que se presenta como recomendaciones.

5. Visualización Interactiva
En grafica_interactiva.py, las recomendaciones se presentan como un grafo interactivo.
• Cada nodo representa una película, y las conexiones reflejan la similitud.
• Se utiliza la biblioteca Plotly para mostrar imágenes de las películas
directamente en el grafo, y una lista adicional muestra las películas recomendadas con su grado de similitud.

7. Interfaz Principal
El archivo main.py coordina todo el flujo:
• Solicita al usuario un filtro de películas por puntuación y un número máximo de películas para visualizar.
• Muestra las películas seleccionadas y permite al usuario elegir una para obtener recomendaciones.
• Finalmente, presenta las recomendaciones en el grafo interactivo.
