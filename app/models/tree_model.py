class Node:
    """
    Clase simple que representa un nodo del árbol.
    
    Atributos:
        value: El valor del nodo
        children: Lista de 2 elementos [izquierdo, derecho]
    """
    def __init__(self, value):
        self.value = value
        self.children = [None, None]  # children[0] = izquierdo, children[1] = derecho
