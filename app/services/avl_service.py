# Servicio AVL Tree (Árbol de Altura Balanceada)
# Este módulo implementa un árbol AVL que se auto-balancea automáticamente.
# Un árbol AVL mantiene el balance de alturas entre subárboles izquierdo y derecho,
# garantizando operaciones de inserción, búsqueda y eliminación en tiempo O(log n).
# El balanceo se logra mediante rotaciones simples (izquierda/derecha) y dobles (LR/RL).

from app.models.avl_model import AVLNode


class AVLTree:
    """Clase para manejar el Árbol AVL (Árbol de Altura Balanceada)"""
    
    def __init__(self):
        self.root = None  # La raíz del árbol
        self.saved_data = []  # Lista para guardar todos los valores insertados
    
    def _get_height(self, node):
        """Obtiene la altura de un nodo"""
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node):
        """Calcula el factor de balance de un nodo (altura izquierda - altura derecha)"""
        if node is None:
            return 0
        return self._get_height(node.children[0]) - self._get_height(node.children[1])
    
    def _update_height(self, node):
        """Actualiza la altura de un nodo"""
        if node is not None:
            node.height = 1 + max(self._get_height(node.children[0]), 
                                  self._get_height(node.children[1]))
    
    def _rotate_right(self, y):
        """
        Rotación simple a la derecha (Right Rotation)
        Se usa cuando el subárbol izquierdo es más alto (desbalance izquierda-izquierda)
        
        Antes:          Después:
            y               x
           / \             / \
          x   T3    →    T1   y
         / \                 / \
        T1  T2              T2  T3
        
        Pasos:
        1. Guardar el hijo izquierdo de y (lo llamamos x)
        2. Guardar el hijo derecho de x (lo llamamos T2)
        3. x sube y se convierte en la nueva raíz
        4. y baja y se convierte en hijo derecho de x
        5. T2 pasa a ser hijo izquierdo de y
        """
        x = y.children[0]  # x es el hijo izquierdo de y
        T2 = x.children[1]  # T2 es el subárbol derecho de x
        
        # Realizar rotación: x sube, y baja
        x.children[1] = y  # y se convierte en hijo derecho de x
        y.children[0] = T2  # T2 se convierte en hijo izquierdo de y
        
        # Actualizar alturas (primero y, luego x)
        self._update_height(y)
        self._update_height(x)
        
        return x  # x es la nueva raíz
    
    def _rotate_left(self, x):
        """
        Rotación simple a la izquierda (Left Rotation)
        Se usa cuando el subárbol derecho es más alto (desbalance derecha-derecha)
        
        Antes:        Después:
          x               y
         / \             / \
        T1  y     →     x   T3
           / \         / \
          T2  T3      T1  T2
        
        Pasos:
        1. Guardar el hijo derecho de x (lo llamamos y)
        2. Guardar el hijo izquierdo de y (lo llamamos T2)
        3. y sube y se convierte en la nueva raíz
        4. x baja y se convierte en hijo izquierdo de y
        5. T2 pasa a ser hijo derecho de x
        """
        y = x.children[1]  # y es el hijo derecho de x
        T2 = y.children[0]  # T2 es el subárbol izquierdo de y
        
        # Realizar rotación: y sube, x baja
        y.children[0] = x  # x se convierte en hijo izquierdo de y
        x.children[1] = T2  # T2 se convierte en hijo derecho de x
        
        # Actualizar alturas (primero x, luego y)
        self._update_height(x)
        self._update_height(y)
        
        return y  # y es la nueva raíz
    
    def insert(self, value):
        """Inserta un valor en el árbol AVL y lo balancea automáticamente"""
        # Guardar el valor en la lista
        if value not in self.saved_data:
            self.saved_data.append(value)
        
        # Si el árbol está vacío, crear la raíz
        if self.root is None:
            self.root = AVLNode(value)
            return True
        
        # Verificar si el valor ya existe
        if self.search(value):
            return False
        
        # Insertar y balancear
        self.root = self._insert_recursive(self.root, value)
        return True
    
    def _insert_recursive(self, node, value):
        """Función recursiva para insertar un valor y balancear"""
        # Si llegamos a None, crear el nuevo nodo
        if node is None:
            return AVLNode(value)
        
        # Insertar recursivamente
        if value < node.value:
            node.children[0] = self._insert_recursive(node.children[0], value)
        elif value > node.value:
            node.children[1] = self._insert_recursive(node.children[1], value)
        else:
            # El valor ya existe, no insertar
            return node
        
        # Actualizar la altura del nodo actual
        self._update_height(node)
        
        # Obtener el factor de balance (balance > 1 = izquierda pesada, balance < -1 = derecha pesada)
        balance = self._get_balance(node)
        
        # ============================================
        # 4 CASOS DE BALANCEO EN ÁRBOL AVL
        # ============================================
        
        # CASO 1: Rotación simple derecha (Left-Left Case)
        # Ocurre cuando se inserta en el subárbol izquierdo del hijo izquierdo
        # El árbol está "cargado" hacia la izquierda-izquierda
        #     z                y
        #    / \              / \
        #   y   T4    →      x   z
        #  / \              / \ / \
        # x  T3            T1 T2 T3 T4
        if balance > 1 and value < node.children[0].value:
            return self._rotate_right(node)
        
        # CASO 2: Rotación simple izquierda (Right-Right Case)
        # Ocurre cuando se inserta en el subárbol derecho del hijo derecho
        # El árbol está "cargado" hacia la derecha-derecha
        #   z                  y
        #  / \                / \
        # T1  y      →       z   x
        #    / \            / \ / \
        #   T2  x          T1 T2 T3 T4
        if balance < -1 and value > node.children[1].value:
            return self._rotate_left(node)
        
        # CASO 3: Rotación doble izquierda-derecha (Left-Right Case)
        # Ocurre cuando se inserta en el subárbol derecho del hijo izquierdo
        # Primero rotamos el hijo izquierdo a la izquierda, luego el nodo a la derecha
        #     z              z                x
        #    / \            / \              / \
        #   y   T4   →     x   T4    →      y   z
        #  / \            / \              / \ / \
        # T1  x          y  T3            T1 T2 T3 T4
        #    / \        / \
        #   T2 T3      T1 T2
        if balance > 1 and value > node.children[0].value:
            node.children[0] = self._rotate_left(node.children[0])  # Primera rotación
            return self._rotate_right(node)  # Segunda rotación
        
        # CASO 4: Rotación doble derecha-izquierda (Right-Left Case)
        # Ocurre cuando se inserta en el subárbol izquierdo del hijo derecho
        # Primero rotamos el hijo derecho a la derecha, luego el nodo a la izquierda
        #   z                z                 x
        #  / \              / \               / \
        # T1  y      →     T1  x      →      z   y
        #    / \              / \            / \ / \
        #   x  T4            T2  y          T1 T2 T3 T4
        #  / \                  / \
        # T2 T3                T3 T4
        if balance < -1 and value < node.children[1].value:
            node.children[1] = self._rotate_right(node.children[1])  # Primera rotación
            return self._rotate_left(node)  # Segunda rotación
        
        return node
    
    def search(self, value):
        """Busca un valor en el árbol"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Función recursiva para buscar un valor"""
        if node is None:
            return False
        
        if value == node.value:
            return True
        
        if value < node.value:
            return self._search_recursive(node.children[0], value)
        else:
            return self._search_recursive(node.children[1], value)
    
    def prune(self, value):
        """Poda (elimina) un valor del árbol y lo balancea"""
        if value in self.saved_data:
            self.saved_data.remove(value)
        
        self.root = self._prune_recursive(self.root, value)
        return True
    
    def _prune_recursive(self, node, value):
        """Función recursiva para podar (eliminar) un valor y balancear"""
        if node is None:
            return None
        
        # Buscar el nodo a eliminar
        if value < node.value:
            node.children[0] = self._prune_recursive(node.children[0], value)
        elif value > node.value:
            node.children[1] = self._prune_recursive(node.children[1], value)
        else:
            # Encontramos el nodo a eliminar
            
            # Caso 1: Nodo sin hijos o con un solo hijo
            if node.children[0] is None:
                return node.children[1]
            elif node.children[1] is None:
                return node.children[0]
            
            # Caso 2: Nodo con dos hijos
            # Encontrar el sucesor inorden (el menor del subárbol derecho)
            min_node = self._find_minimum(node.children[1])
            node.value = min_node.value
            node.children[1] = self._prune_recursive(node.children[1], min_node.value)
        
        # Si el árbol tiene un solo nodo
        if node is None:
            return node
        
        # Actualizar la altura del nodo actual
        self._update_height(node)
        
        # Obtener el factor de balance
        balance = self._get_balance(node)
        
        # Rebalancear el árbol
        # Caso 1: Left-Left
        if balance > 1 and self._get_balance(node.children[0]) >= 0:
            return self._rotate_right(node)
        
        # Caso 2: Right-Right
        if balance < -1 and self._get_balance(node.children[1]) <= 0:
            return self._rotate_left(node)
        
        # Caso 3: Left-Right
        if balance > 1 and self._get_balance(node.children[0]) < 0:
            node.children[0] = self._rotate_left(node.children[0])
            return self._rotate_right(node)
        
        # Caso 4: Right-Left
        if balance < -1 and self._get_balance(node.children[1]) > 0:
            node.children[1] = self._rotate_right(node.children[1])
            return self._rotate_left(node)
        
        return node
    
    def _find_minimum(self, node):
        """Encuentra el nodo con el valor mínimo"""
        current = node
        while current.children[0] is not None:
            current = current.children[0]
        return current
    
    def balance_tree(self):
        """Balancea completamente el árbol desde cero"""
        if self.root is None:
            return
        
        # Obtener todos los valores en orden
        values = self.inorder()
        
        # Reconstruir el árbol balanceado
        self.root = None
        self.root = self._build_balanced_tree(values, 0, len(values) - 1)
    
    def _build_balanced_tree(self, values, start, end):
        """Construye un árbol balanceado desde una lista ordenada"""
        if start > end:
            return None
        
        # Tomar el elemento del medio como raíz
        mid = (start + end) // 2
        node = AVLNode(values[mid])
        
        # Construir recursivamente los subárboles
        node.children[0] = self._build_balanced_tree(values, start, mid - 1)
        node.children[1] = self._build_balanced_tree(values, mid + 1, end)
        
        # Actualizar la altura
        self._update_height(node)
        
        return node
    
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
        """Convierte un nodo a diccionario con información de altura"""
        if node is None:
            return None
        
        return {
            "value": node.value,
            "height": node.height,
            "balance": self._get_balance(node),
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


# Instancia global del árbol AVL
avl_tree = AVLTree()
