from app.models.tree_model import Node
from app.models.kid_model import Kid


class BinarySearchTree:
    """Clase para manejar el Árbol Binario de Búsqueda"""
    
    def __init__(self):
        self.root = None  # La raíz del árbol
        self.saved_data = []  # Lista para guardar todos los IDs insertados
    
    def insert(self, kid_id: int, name: str = "", age: int = 0):
        """Inserta un Kid en el árbol
        
        Args:
            kid_id: Identificador único del Kid
            name: Nombre del Kid (opcional)
            age: Edad del Kid (opcional)
        
        El árbol usa el ID del Kid para determinar automáticamente
        si va a la izquierda (ID menor) o derecha (ID mayor).
        """
        # Guardar el ID en la lista
        if kid_id not in self.saved_data:
            self.saved_data.append(kid_id)
        
        # Crear el Kid con ID, name y age
        kid = Kid(kid_id, name, age)
        
        # Si el árbol está vacío, crear la raíz
        if self.root is None:
            self.root = Node(kid)
            return True
        
        # Si no está vacío, buscar dónde insertar
        # El árbol decide izquierda/derecha comparando IDs
        return self._insert_recursive(self.root, kid)
    
    def _insert_recursive(self, current_node, kid):
        """Función recursiva para insertar un Kid"""
        # Si el ID ya existe, no insertarlo
        if kid.id == current_node.kid.id:
            return False
        
        # Si el ID es menor, va al hijo izquierdo (children[0])
        if kid.id < current_node.kid.id:
            if current_node.children[0] is None:
                current_node.children[0] = Node(kid)
                return True
            else:
                return self._insert_recursive(current_node.children[0], kid)
        
        # Si el ID es mayor, va al hijo derecho (children[1])
        else:
            if current_node.children[1] is None:
                current_node.children[1] = Node(kid)
                return True
            else:
                return self._insert_recursive(current_node.children[1], kid)
    
    def search(self, kid_id: int):
        """Busca un Kid por ID en el árbol"""
        return self._search_recursive(self.root, kid_id)
    
    def _search_recursive(self, current_node, kid_id):
        """Función recursiva para buscar un Kid por ID"""
        # Si llegamos a None, el ID no existe
        if current_node is None:
            return False
        
        # Si encontramos el ID
        if kid_id == current_node.kid.id:
            return True
        
        # Si el ID es menor, buscar en el hijo izquierdo (children[0])
        if kid_id < current_node.kid.id:
            return self._search_recursive(current_node.children[0], kid_id)
        
        # Si el ID es mayor, buscar en el hijo derecho (children[1])
        else:
            return self._search_recursive(current_node.children[1], kid_id)
    
    def prune(self, kid_id: int):
        """Poda (elimina) un Kid del árbol por ID"""
        if kid_id in self.saved_data:
            self.saved_data.remove(kid_id)
        
        self.root = self._prune_recursive(self.root, kid_id)
        return True
    
    def _prune_recursive(self, current_node, kid_id):
        """Función recursiva para podar (eliminar) un Kid"""
        # Si el nodo es None, no hay nada que podar
        if current_node is None:
            return None
        
        # Buscar el nodo a podar
        if kid_id < current_node.kid.id:
            current_node.children[0] = self._prune_recursive(current_node.children[0], kid_id)
        elif kid_id > current_node.kid.id:
            current_node.children[1] = self._prune_recursive(current_node.children[1], kid_id)
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
            # Encontrar el Kid con el ID más pequeño en el subárbol derecho
            min_node = self._find_minimum(current_node.children[1])
            current_node.kid = min_node.kid
            current_node.children[1] = self._prune_recursive(current_node.children[1], min_node.kid.id)
        
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
            result.append(node.kid.id)
            self._inorder_recursive(node.children[1], result)
    
    def preorder(self):
        """Recorrido preorden: raíz -> izquierda -> derecha"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Función recursiva para recorrido preorden"""
        if node is not None:
            result.append(node.kid.id)
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
            result.append(node.kid.id)
    
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
            "kid": {
                "id": node.kid.id,
                "name": node.kid.name,
                "age": node.kid.age
            },
            "children": [
                self._node_to_dict(node.children[0]),
                self._node_to_dict(node.children[1])
            ]
        }
    
    def _collect_kids_by_age(self, node, min_age, result):
        """Función recursiva para recolectar Kids por edad (recorrido inorden)"""
        if node is not None:
            # Recorrer izquierda
            self._collect_kids_by_age(node.children[0], min_age, result)
            
            # Procesar nodo actual
            if node.kid.age >= min_age:
                result.append({
                    "id": node.kid.id,
                    "name": node.kid.name,
                    "age": node.kid.age
                })
            
            # Recorrer derecha
            self._collect_kids_by_age(node.children[1], min_age, result)
    
    def get_kids_grouped_by_age_ranges(self, range_size: int):
        """Agrupa los Kids por rangos de edad
        
        Args:
            range_size: Tamaño del rango de edad. Por ejemplo, si es 3:
                       0-3, 4-6, 7-9, 10-12, etc.
        
        Returns:
            Lista de diccionarios con el rango y la cantidad de Kids en ese rango
        """
        if range_size <= 0:
            return []
        
        # Recolectar todas las edades
        ages_dict = {}
        self._collect_all_ages(self.root, ages_dict)
        
        if not ages_dict:
            return []
        
        # Encontrar edad mínima y máxima
        min_age = min(ages_dict.keys())
        max_age = max(ages_dict.keys())
        
        # Agrupar por rangos
        ranges = []
        current_start = 0
        
        while current_start <= max_age:
            current_end = current_start + range_size
            range_key = f"{current_start}-{current_end}"
            
            # Contar Kids en este rango
            count = sum(ages_dict.get(age, 0) for age in range(current_start, current_end + 1))
            
            if count > 0:
                ranges.append({
                    "range": range_key,
                    "quantity": count
                })
            
            current_start = current_end + 1
        
        return ranges
    
    def _collect_all_ages(self, node, ages_dict):
        """Función recursiva para recolectar todas las edades y contarlas"""
        if node is not None:
            # Recorrer izquierda
            self._collect_all_ages(node.children[0], ages_dict)
            
            # Contar edad del nodo actual
            age = node.kid.age
            if age in ages_dict:
                ages_dict[age] += 1
            else:
                ages_dict[age] = 1
            
            # Recorrer derecha
            self._collect_all_ages(node.children[1], ages_dict)
    
    def get_saved_data(self):
        """Retorna todos los datos que han sido insertados"""
        return self.saved_data
    
    def clear(self):
        """Limpia todo el árbol"""
        self.root = None
        self.saved_data = []


    def create_sample_tree(self):
        """Crea un árbol de ejemplo con Kids predefinidos.
        
        Returns:
            BinarySearchTree: Una instancia del árbol con Kids de ejemplo.
        """
        sample_tree = BinarySearchTree()
        # Insertar Kids de ejemplo
        ids = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90]
        for kid_id in ids:
            sample_tree.insert(kid_id)
        return sample_tree

# Instancia global del árbol
tree = BinarySearchTree()
