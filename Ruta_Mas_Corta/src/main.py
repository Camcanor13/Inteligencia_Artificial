# 5. Ejecución del Código
import sys
sys.path.append('src/')  # Asegúrate de que esta ruta es correcta
from Graph import create_city_graph
from bfs import bfs
from utils import animate_route, get_user_input

def main():
    G = create_city_graph()

    start, goal = get_user_input()

    if start and goal:
        start = start.strip().upper()
        goal = goal.strip().upper()

        if start not in G.nodes or goal not in G.nodes:
            print("Nodos inválidos. Asegúrate de que los nodos estén en la lista.")
        else:
            bfs_path = bfs(G, start, goal)

            if bfs_path:
                animate_route(G, bfs_path)
            else:
                print(f"No se encontró un camino entre {start} y {goal}.")
    else:
        print("Entrada no válida.")

if __name__ == "__main__":
    main()
