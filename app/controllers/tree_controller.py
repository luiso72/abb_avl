from fastapi import APIRouter
from app.services.tree_service import tree

router = APIRouter(prefix="/tree", tags=["Binary Search Tree"])


@router.post("/insert")
def insert_kid(kid_id: int, name: str = "", age: int = 0):
    """Inserta un Kid en el árbol con ID, nombre y edad
    
    Args:
        kid_id: Identificador único del Kid (requerido)
        name: Nombre del Kid (opcional)
        age: Edad del Kid (opcional)
    
    El árbol decide automáticamente si el Kid va a la izquierda o derecha
    comparando su ID con los IDs de otros Kids en el árbol.
    """
    success = tree.insert(kid_id, name, age)
    
    if success:
        return {
            "message": f"Kid inserted successfully",
            "success": True,
            "data": {
                "kid": {
                    "id": kid_id,
                    "name": name,
                    "age": age
                },
                "structure": tree.get_structure()
            }
        }
    else:
        return {
            "message": f"Kid {kid_id} already exists in the tree",
            "success": False
        }


@router.post("/kidsbyagerange")
def kids_by_age_range(min_age: int):
    """Obtiene todos los Kids con edad mayor o igual a min_age
    
    Args:
        min_age: Edad mínima (inclusive). Por ejemplo, si se inserta 8,
                 devolverá todos los Kids con edad >= 8 (del 8 al mayor)
    
    Returns:
        Lista de Kids ordenados por ID que cumplen con el rango de edad
    """
    kids = tree.get_kids_by_age_range(min_age)
    
    if len(kids) == 0:
        return {
            "message": f"No Kids found with age >= {min_age}",
            "success": True,
            "data": {
                "min_age": min_age,
                "count": 0,
                "kids": []
            }
        }
    
    return {
        "message": f"Found {len(kids)} Kids with age >= {min_age}",
        "success": True,
        "data": {
            "min_age": min_age,
            "count": len(kids),
            "kids": kids
        }
    }


@router.post("/kidsbygroupedages")
def kids_by_grouped_ages(range_size: int):
    """Agrupa los Kids por rangos de edad y muestra la cantidad en cada rango
    
    Args:
        range_size: Tamaño del rango de edad. Por ejemplo:
                   - Si range_size=3: agrupa en 0-3, 4-6, 7-9, 10-12, etc.
                   - Si range_size=5: agrupa en 0-5, 6-10, 11-15, etc.
    
    Returns:
        Lista de rangos con la cantidad de Kids en cada uno
        Ejemplo: [{"range": "0-3", "quantity": 4}, {"range": "4-6", "quantity": 2}]
    """
    if range_size <= 0:
        return {
            "message": "Range size must be greater than 0",
            "success": False,
            "data": {"ranges": []}
        }
    
    ranges = tree.get_kids_grouped_by_age_ranges(range_size)
    
    total_kids = sum(r['quantity'] for r in ranges)
    
    return {
        "message": f"Kids grouped by age ranges of {range_size}",
        "success": True,
        "data": {
            "range_size": range_size,
            "total_kids": total_kids,
            "ranges": ranges
        }
    }


@router.post("/search")
def search_kid(kid_id: int):
    """Busca un Kid por ID en el árbol"""
    found = tree.search(kid_id)
    
    return {
        "message": f"Kid {kid_id} {'found' if found else 'not found'}",
        "success": found,
        "data": {"found": found}
    }


@router.delete("/prune")
def prune_kid(kid_id: int):
    """Elimina un Kid del árbol por ID (poda un nodo)"""
    # First check if it exists
    exists = tree.search(kid_id)
    
    if exists:
        tree.prune(kid_id)
        return {
            "message": f"Kid {kid_id} pruned successfully",
            "success": True,
            "data": {"structure": tree.get_structure()}
        }
    else:
        return {
            "message": f"Kid {kid_id} does not exist in the tree",
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
    """Muestra todos los IDs de Kids guardados en el árbol"""
    data = tree.get_saved_data()
    
    return {
        "message": "Saved Kid IDs in the tree",
        "success": True,
        "data": {"kid_ids": data}
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
