import networkx as nx
import plotly.graph_objects as go
import pandas as pd

def create_graph_and_list(movie_title, recommendations, movies):
    """
    Crea una gráfica interactiva basada en las recomendaciones de películas y
    muestra una lista al lado del grafo.
    """
    G = nx.Graph()
    
    # Nodo principal
    main_image = movies.loc[movies["title"] == movie_title, "image"].iloc[0] if not movies[movies["title"] == movie_title].empty else None
    G.add_node(movie_title, size=50, image=main_image)

    # Nodos recomendados
    for rec_movie, similarity in recommendations.items():
        rec_image = movies.loc[movies["title"] == rec_movie, "image"].iloc[0] if not movies[movies["title"] == rec_movie].empty else None
        G.add_node(rec_movie, size=50, similarity=similarity, image=rec_image)
        G.add_edge(movie_title, rec_movie, weight=similarity)

    pos = nx.spring_layout(G, seed=42, k=1.2)

    node_x = [pos[node][0] for node in G.nodes()]
    node_y = [pos[node][1] for node in G.nodes()]
    node_labels = list(G.nodes())

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    fig = go.Figure()

    # Añadir aristas
    fig.add_trace(go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.8, color='gray'),
        hoverinfo='none',
        mode='lines'
    ))

    # Añadir nodos
    for x, y, label in zip(node_x, node_y, node_labels):
        image = G.nodes[label].get("image")
        if image:
            fig.add_layout_image(
                dict(
                    source=image,
                    x=x, y=y,
                    xref="x", yref="y",
                    sizex=1.0, sizey=1.0,
                    xanchor="center", yanchor="middle",
                    layer="above"
                )
            )

    fig.update_layout(
        title=f"Recomendaciones para '{movie_title}'",
        xaxis=dict(showgrid=False, zeroline=False, range=[-2.5, 2.5]),
        yaxis=dict(showgrid=False, zeroline=False, range=[-2.5, 2.5]),
        showlegend=False,
        width=800,
        height=800
    )

    # Mostrar lista de recomendaciones
    print(f"\nRecomendaciones para '{movie_title}':")
    print("\nPelícula recomendada - Similitud")
    for movie, similarity in recommendations.items():
        print(f"{movie} - {similarity:.2f}")

    fig.show()

if __name__ == "__main__":
    # Cargar las películas
    movies = pd.read_csv("movies_with_images.csv")

    # Mostrar las películas cargadas
    print("Películas disponibles:")
    print(movies[["title", "genres"]].to_string(index=False))

    # Elegir una película
    selected_movie = input("\nEscriba el título exacto de una película de la lista: ")

    # Crear gráfica interactiva y mostrar la lista
    create_graph_and_list(selected_movie, recommendations, movies)
