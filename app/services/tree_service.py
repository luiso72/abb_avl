from app.models.tree_model import Node


class BinarySearchTree:
    """Clase para manejar el Árbol Binario de Búsqueda"""
    
    def __init__(self):
        self.root = None  # La raíz del árbol
        self.saved_data = []  # Lista para guardar todos los valores insertados
    
    def insert(self, value):
        """Inserta un valor en el árbol"""
        # Guardar el valor en la lista
        if value not in self.saved_data:
            self.saved_data.append(value)
        
        # Si el árbol está vacío, crear la raíz
        if self.root is None:
            self.root = Node(value)
            return True
        
        # Si no está vacío, buscar dónde insertar
        return self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current_node, value):
        """Función recursiva para insertar un valor"""
        # Si el valor ya existe, no insertarlo
        if value == current_node.value:
            return False
        
        # Si el valor es menor, va al hijo izquierdo (children[0])
        if value < current_node.value:
            if current_node.children[0] is None:
                current_node.children[0] = Node(value)
                return True
            else:
                return self._insert_recursive(current_node.children[0], value)
        
        # Si el valor es mayor, va al hijo derecho (children[1])
        else:
            if current_node.children[1] is None:
                current_node.children[1] = Node(value)
                return True
            else:
                return self._insert_recursive(current_node.children[1], value)
    
    def search(self, value):
        """Busca un valor en el árbol"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, current_node, value):
        """Función recursiva para buscar un valor"""
        # Si llegamos a None, el valor no existe
        if current_node is None:
            return False
        
        # Si encontramos el valor
        if value == current_node.value:
            return True
        
        # Si el valor es menor, buscar en el hijo izquierdo (children[0])
        if value < current_node.value:
            return self._search_recursive(current_node.children[0], value)
        
        # Si el valor es mayor, buscar en el hijo derecho (children[1])
        else:
            return self._search_recursive(current_node.children[1], value)
    
    def prune(self, value):
        """Poda (elimina) un valor del árbol"""
        if value in self.saved_data:
            self.saved_data.remove(value)
        
        self.root = self._prune_recursive(self.root, value)
        return True
    
    def _prune_recursive(self, current_node, value):
        """Función recursiva para podar (eliminar) un valor"""
        # Si el nodo es None, no hay nada que podar
        if current_node is None:
            return None
        
        # Buscar el nodo a podar
        if value < current_node.value:
            current_node.children[0] = self._prune_recursive(current_node.children[0], value)
        elif value > current_node.value:
            current_node.children[1] = self._prune_recursive(current_node.children[1], value)
        else:
            # Encontramos el nodo a podar
            
            # Caso 1: El nodo no tiene hijos
            if current_node.children[0] is None and current_node.children[1] is None:
                return None
            
            # Caso 2: El nodo solo tiene hijo derecho
            if current_node.children[0] is None:
                return current_node.children[1]
            
            # Caso 3: El nodo solo tiene hijo izquierdo
            if current_node.children[1] is None:
                return current_node.children[0]
            
            # Caso 4: El nodo tiene dos hijos
            # Encontrar el valor más pequeño en el subárbol derecho
            min_node = self._find_minimum(current_node.children[1])
            current_node.value = min_node.value
            current_node.children[1] = self._prune_recursive(current_node.children[1], min_node.value)
        
        return current_node
    
    def _find_minimum(self, node):
        """Encuentra el nodo con el valor mínimo"""
        current = node
        while current.children[0] is not None:
            current = current.children[0]
        return current
    
    def inorder(self):
        """Recorrido inorden: izquierda -> raíz -> derecha"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Función recursiva para recorrido inorden"""
        if node is not None:
            self._inorder_recursive(node.children[0], result)
            result.append(node.value)
            self._inorder_recursive(node.children[1], result)
    
    def preorder(self):
        """Recorrido preorden: raíz -> izquierda -> derecha"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Función recursiva para recorrido preorden"""
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.children[0], result)
            self._preorder_recursive(node.children[1], result)
    
    def postorder(self):
        """Recorrido postorden: izquierda -> derecha -> raíz"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """Función recursiva para recorrido postorden"""
        if node is not None:
            self._postorder_recursive(node.children[0], result)
            self._postorder_recursive(node.children[1], result)
            result.append(node.value)
    
    def get_structure(self):
        """Obtiene la estructura del árbol en formato diccionario"""
        if self.root is None:
            return None
        return self._node_to_dict(self.root)
    
    def _node_to_dict(self, node):
        """Convierte un nodo a diccionario"""
        if node is None:
            return None
        
        return {
            "value": node.value,
            "children": [
                self._node_to_dict(node.children[0]),
                self._node_to_dict(node.children[1])
            ]
        }
    
    def get_saved_data(self):
        """Retorna todos los datos que han sido insertados"""
        return self.saved_data
    
    def clear(self):
        """Limpia todo el árbol"""
        self.root = None
        self.saved_data = []


    def create_sample_tree(self):
        """Crea un árbol de ejemplo con valores predefinidos.
        
        Returns:
            BinarySearchTree: Una instancia del árbol con valores de ejemplo.
        """
        sample_tree = BinarySearchTree()
        # Insertar valores de ejemplo
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90]
        for value in values:
            sample_tree.insert(value)
        return sample_tree

# Instancia global del árbol
tree = BinarySearchTree()
