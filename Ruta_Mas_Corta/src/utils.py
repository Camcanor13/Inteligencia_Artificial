import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
from tkinter import simpledialog

def animate_route(graph, path):
    pos = {
        "A": (0, 1), "B": (1, 2), "C": (1, 1), "D": (2, 2),
        "E": (2, 1), "F": (3, 1), "G": (4, 1), "H": (3, 0)
    }

    fig, ax = plt.subplots(figsize=(10, 8))
    current_step = 0

    def update():
        ax.clear()
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color='lightblue', 
                font_size=16, font_color='black', font_weight='bold', edge_color='grey')

        if current_step < len(path):
            path_edges = [(path[i], path[i + 1]) for i in range(current_step)]
            nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='orange', width=3)
        
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red')
        plt.title(f'Animación de la Ruta: {path[:current_step + 1]}', fontsize=18)
        plt.draw()

    def on_key(event):
        nonlocal current_step
        if event.key == 'enter':
            if current_step < len(path) - 1:
                current_step += 1
                update()

    fig.canvas.mpl_connect('key_press_event', on_key)
    update()
    plt.show()

def get_user_input():
    root = tk.Tk()
    root.withdraw()
    start = simpledialog.askstring("Nodo de Inicio", "Ingresa el nodo de inicio (A, B, C, D, E, F, G, H):")
    goal = simpledialog.askstring("Nodo Objetivo", "Ingresa el nodo objetivo (A, B, C, D, E, F, G, H):")
    root.destroy()
    return start, goal
