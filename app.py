import os
from typing import Union
from fastapi import FastAPI

app = FastAPI()

def read_file_content(path: str) -> str:
    """Lee el contenido de un archivo si existe, de lo contrario devuelve un error."""
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return f"Error: File not found at {path}"

@app.get("/env")
def get_environment_variables():
    """
    Devuelve todas las variables de entorno, incluyendo las extraídas
    de ConfigMap y Secret según las rutas especificadas.
    """
    # 1. Obtener todas las variables del sistema
    env_vars = dict(os.environ)

    # 2. Agregar variables específicas desde los volúmenes
    env_vars["application.properties.from.configmap"] = read_file_content("/config/application.properties")
    env_vars["application.secret.properties.from.secret"] = read_file_content("/secret-config/application.secret.properties")

    return env_vars

@app.get("/")
def read_root():
    """Returns Hello World."""
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, item_count: Union[str, None] = None):
    """Returns numbers of items."""
    return {"item_id": item_id, "q": item_count}
