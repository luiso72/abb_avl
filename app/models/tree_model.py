from app.models.kid_model import Kid


class Node:
    """
    Clase simple que representa un nodo del árbol.
    
    Atributos:
        kid: El Kid almacenado en el nodo
        children: Lista de 2 elementos [izquierdo, derecho] - nodos hijos en el árbol
    """
    def __init__(self, kid: Kid):
        self.kid = kid
        self.children = [None, None]  # children[0] = izquierdo, children[1] = derecho
