from fastapi import FastAPI
from app.controllers.tree_controller import router as bst_router
from app.controllers.avl_controller import router as avl_router

app = FastAPI(
    title="API de Árboles Binarios",
    description="API para gestionar Árbol Binario de Búsqueda (BST) y Árbol AVL",
    version="1.0.0"
)

# Incluir los routers de los árboles
app.include_router(bst_router)
app.include_router(avl_router)


@app.get("/")
def home():
    """Página de inicio"""
    return {
        "message": "Bienvenido a la API de Árboles Binarios",
        "trees": {
            "bst": "Binary Search Tree - /tree",
            "avl": "AVL Tree - /avl"
        },
        "documentation": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
