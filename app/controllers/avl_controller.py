from fastapi import APIRouter
from app.services.avl_service import avl_tree

router = APIRouter(prefix="/avl", tags=["AVL Tree"])


@router.post("/insert")
def insert_value(value: int):
    """Inserta un valor en el árbol AVL (balancea automáticamente)"""
    success = avl_tree.insert(value)
    
    if success:
        return {
            "message": f"Value {value} inserted and tree balanced successfully",
            "success": True,
            "data": {"structure": avl_tree.get_structure()}
        }
    else:
        return {
            "message": f"Value {value} already exists in the tree",
            "success": False
        }


@router.post("/search")
def search_value(value: int):
    """Busca un valor en el árbol AVL"""
    found = avl_tree.search(value)
    
    return {
        "message": f"Value {value} {'found' if found else 'not found'}",
        "success": found,
        "data": {"found": found}
    }


@router.delete("/prune")
def prune_value(value: int):
    """Elimina un valor del árbol AVL (poda y rebalancea automáticamente)"""
    exists = avl_tree.search(value)
    
    if exists:
        avl_tree.prune(value)
        return {
            "message": f"Value {value} pruned and tree rebalanced successfully",
            "success": True,
            "data": {"structure": avl_tree.get_structure()}
        }
    else:
        return {
            "message": f"Value {value} does not exist in the tree",
            "success": False
        }


@router.post("/balance")
def balance_tree():
    """Fuerza un rebalanceo completo del árbol AVL"""
    if avl_tree.root is None:
        return {
            "message": "The tree is empty, nothing to balance",
            "success": False
        }
    
    avl_tree.balance_tree()
    return {
        "message": "Tree balanced successfully",
        "success": True,
        "data": {"structure": avl_tree.get_structure()}
    }


@router.get("/structure")
def get_structure():
    """Muestra la estructura completa del árbol AVL con alturas y balance"""
    structure = avl_tree.get_structure()
    
    if structure is None:
        return {
            "message": "The tree is empty",
            "success": False,
            "data": {"structure": None}
        }
    
    return {
        "message": "AVL tree structure obtained",
        "success": True,
        "data": {"structure": structure}
    }


@router.get("/traversal/inorder")
def inorder_traversal():
    """Recorrido inorden: izquierda -> raíz -> derecha"""
    result = avl_tree.inorder()
    
    return {
        "message": "Inorder traversal",
        "success": True,
        "data": {"traversal": result}
    }


@router.get("/traversal/preorder")
def preorder_traversal():
    """Recorrido preorden: raíz -> izquierda -> derecha"""
    result = avl_tree.preorder()
    
    return {
        "message": "Preorder traversal",
        "success": True,
        "data": {"traversal": result}
    }


@router.get("/traversal/postorder")
def postorder_traversal():
    """Recorrido postorden: izquierda -> derecha -> raíz"""
    result = avl_tree.postorder()
    
    return {
        "message": "Postorder traversal",
        "success": True,
        "data": {"traversal": result}
    }


@router.get("/saved-data")
def get_saved_data():
    """Muestra todos los datos guardados en el árbol AVL"""
    data = avl_tree.get_saved_data()
    
    return {
        "message": "Saved data in the AVL tree",
        "success": True,
        "data": {"values": data}
    }


@router.delete("/clear")
def clear_tree():
    """Limpia todo el árbol AVL (poda completa)"""
    avl_tree.clear()
    
    return {
        "message": "AVL tree cleared successfully",
        "success": True,
        "data": {"structure": None}
    }
