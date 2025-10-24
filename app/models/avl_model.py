class AVLNode:
    """
    Clase simple que representa un nodo del árbol AVL.
    
    Atributos:
        value: El valor del nodo
        children: Lista de 2 elementos [izquierdo, derecho]
        height: Altura del nodo (usado para balanceo)
    """
    def __init__(self, value):
        self.value = value
        self.children = [None, None]  # children[0] = izquierdo, children[1] = derecho
        self.height = 1  # La altura inicial de un nodo es 1
