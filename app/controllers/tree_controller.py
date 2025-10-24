from fastapi import APIRouter
from app.services.tree_service import tree

router = APIRouter(prefix="/tree", tags=["Binary Search Tree"])


@router.post("/insert")
def insert_value(value: int):
    """Inserta un valor en el árbol"""
    success = tree.insert(value)
    
    if success:
        return {
            "message": f"Value {value} inserted successfully",
            "success": True,
            "data": {"structure": tree.get_structure()}
        }
    else:
        return {
            "message": f"Value {value} already exists in the tree",
            "success": False
        }


@router.post("/search")
def search_value(value: int):
    """Busca un valor en el árbol"""
    found = tree.search(value)
    
    return {
        "message": f"Value {value} {'found' if found else 'not found'}",
        "success": found,
        "data": {"found": found}
    }


@router.delete("/prune")
def prune_value(value: int):
    """Elimina un valor del árbol (poda un nodo)"""
    # First check if it exists
    exists = tree.search(value)
    
    if exists:
        tree.prune(value)
        return {
            "message": f"Value {value} pruned successfully",
            "success": True,
            "data": {"structure": tree.get_structure()}
        }
    else:
        return {
            "message": f"Value {value} does not exist in the tree",
            "success": False
        }


@router.get("/structure")
def get_structure():
    """Muestra la estructura completa del árbol"""
    structure = tree.get_structure()
    
    if structure is None:
        return {
            "message": "The tree is empty",
            "success": False,
            "data": {"structure": None}
        }
    
    return {
        "message": "Tree structure obtained",
        "success": True,
        "data": {"structure": structure}
    }


@router.get("/traversal/inorder")
def inorder_traversal():
    """Recorrido inorden: izquierda -> raíz -> derecha"""
    result = tree.inorder()
    
    return {
        "message": "Inorder traversal",
        "success": True,
        "data": {"traversal": result}
    }


@router.get("/traversal/preorder")
def preorder_traversal():
    """Recorrido preorden: raíz -> izquierda -> derecha"""
    result = tree.preorder()
    
    return {
        "message": "Preorder traversal",
        "success": True,
        "data": {"traversal": result}
    }


@router.get("/traversal/postorder")
def postorder_traversal():
    """Recorrido postorden: izquierda -> derecha -> raíz"""
    result = tree.postorder()
    
    return {
        "message": "Postorder traversal",
        "success": True,
        "data": {"traversal": result}
    }


@router.get("/saved-data")
def get_saved_data():
    """Muestra todos los datos guardados en el árbol"""
    data = tree.get_saved_data()
    
    return {
        "message": "Saved data in the tree",
        "success": True,
        "data": {"values": data}
    }


@router.delete("/clear")
def clear_tree():
    """Limpia todo el árbol (poda completa)"""
    tree.clear()
    
    return {
        "message": "Tree cleared successfully",
        "success": True,
        "data": {"structure": None}
    }
