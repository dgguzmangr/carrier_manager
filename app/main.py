from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def leer_raiz():
    return {"mensaje": "¡Hola, FastAPI!"}

@app.get("/items/{item_id}")
def leer_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
