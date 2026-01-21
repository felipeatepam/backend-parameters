import os
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/env")
def read_env():
    """Returns all environment variables and specific config files."""
    # 1. Start with the current system environment variables (Includes ENV_VAR5)
    env_vars = dict(os.environ)

    # Helper function to safely read files
    def read_file(path):
        if os.path.exists(path):
            with open(path, "r") as f:
                return f.read().strip()
        return "File not found"

    # 2. Read ConfigMap file
    env_vars["application.properties.from.configmap"] = read_file("/config/application.properties")

    # 3. Read Standard Secret file
    env_vars["application.secret.properties.from.secret"] = read_file("/secret-config/application.secret.properties")

    # 4. Read AWS Parameter Store Secret file (NEW)
    env_vars["application.secret.properties.from.ps"] = read_file("/ps-config/application.secret.properties.from.ps")

    return env_vars

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, item_count: Union[str, None] = None):
    return {"item_id": item_id, "q": item_count}
