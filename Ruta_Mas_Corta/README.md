# Ruta Más Corta - Proyecto de Algoritmos de Búsqueda

Este proyecto implementa algoritmos de búsqueda (BFS y A\*) para encontrar la ruta más corta entre ciudades representadas en un grafo. El proyecto también incluye una visualización animada de las rutas calculadas.

## _Requisitos del Sistema_

- Python 3.7 o superior
- Visual Studio Code
- Bibliotecas de Python: `networkx`, `matplotlib`, `tkinter`

## _Instalación_

- Instalar VS Code

- Instalar Python: Puedes descargarlo desde python.org. Asegúrate también de agregar Python al PATH durante la instalación.

Para verificar que Python está instalado correctamente, abre una terminal y escribe:

```
python --version

```

## _Configuración_

1.  Abre el proyecto en VS Code:

    - Abre Visual Studio Code.
    - En el menú, selecciona File > Open Folder....
    - Navega a la carpeta raíz de tu proyecto Ruta_Mas_Corta y ábrela.

2.  Crea un entorno virtual

    - Abre una terminal en VS Code (Terminal > New Terminal)
    - Escribe el siguiente comando para crear un entorno virtual en Python:

    ```
    python -m venv venv

    ```

    - Activa el entorno virtual(Windows):

    ```
    venv\Scripts\activate

    ```

3.  Instalar dependencias

    - El proyecto utiliza networkx para el manejo de grafos, matplotlib para la visualización y tkinter para ventanas emergentes

    ```
    pip install networkx matplotlib

    ```

4.  Ejecutar el Proyecto

    - Asegúrate de estar en el archivo main.py dentro de la carpeta src/
    - En la terminal de VS Code, ejecuta el siguiente comando para correr el archivo:

    ```
    python src/main.py

    ```
