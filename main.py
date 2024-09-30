import tkinter as tk
from tkinter import simpledialog
import networkx as nx

# Crear un grafo vacío
G = nx.Graph()

# Función para agregar rutas al grafo
def agregar_ruta(grafo, origen, destino, peso):
    grafo.add_edge(origen, destino, weight=peso)

# Agregar nodos y aristas (ejemplo de un sistema de transporte masivo)
agregar_ruta(G, 'Estación A', 'Estación B', 5)   # 5 minutos
agregar_ruta(G, 'Estación A', 'Estación C', 10)  # 10 minutos
agregar_ruta(G, 'Estación B', 'Estación D', 3)   # 3 minutos
agregar_ruta(G, 'Estación C', 'Estación D', 4)   # 4 minutos
agregar_ruta(G, 'Estación D', 'Estación E', 2)   # 2 minutos
agregar_ruta(G, 'Estación B', 'Estación E', 8)   # 8 minutos

def encontrar_ruta_mejor(grafo, inicio, fin):
    return nx.dijkstra_path(grafo, inicio, fin)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculador de Rutas del Transporte Masivo")
ventana.geometry("400x300")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="¡Bienvenido al Calculador de Rutas!")
etiqueta.pack(pady=10)

# Función para solicitar puntos y mostrar la ruta
def solicitar_puntos():
    punto_partida = simpledialog.askstring("Entrada", "Ingrese la estación de partida (Estación A,B,C o D):")
    punto_destino = simpledialog.askstring("Entrada", "Ingrese la estación de destino(Estación A,B,C o D):")
    
    if punto_partida and punto_destino:
        try:
            ruta = encontrar_ruta_mejor(G, punto_partida, punto_destino)
            tiempo_total = sum(G[u][v]['weight'] for u, v in zip(ruta[:-1], ruta[1:]))
            etiqueta.config(text=f"La mejor ruta desde {punto_partida} a {punto_destino} es: {ruta} \nTiempo total: {tiempo_total} minutos.")
        except nx.NetworkXNoPath:
            etiqueta.config(text="No hay ruta disponible entre los puntos especificados.")
        except Exception as e:
            etiqueta.config(text=str(e))
    else:
        etiqueta.config(text="Por favor, ingrese ambos puntos.")

# Botón para solicitar puntos
boton_solicitar = tk.Button(ventana, text="Solicitar Puntos", command=solicitar_puntos)
boton_solicitar.pack(pady=10)

# Crear un botón que cierra la aplicación
boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
boton_salir.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()