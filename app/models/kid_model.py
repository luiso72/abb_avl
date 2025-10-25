class Kid:
    """
    Clase que representa un Kid (niño).
    
    Atributos:
        id: Identificador único del Kid
        name: Nombre del Kid
        age: Edad del Kid
    
    Nota: left y right no son atributos del Kid, sino que el árbol (ABB)
    usa el ID del Kid para determinar si va a la izquierda o derecha basándose
    en comparaciones de IDs.
    """
    def __init__(self, id: int, name: str = "", age: int = 0):
        self.id = id
        self.name = name
        self.age = age
    
    def to_dict(self):
        """Convierte el Kid a un diccionario para JSON"""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }
    
    def __str__(self):
        return f"Kid(id={self.id}, name='{self.name}', age={self.age})"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if isinstance(other, Kid):
            return self.id == other.id
        return False
    
    def __lt__(self, other):
        """Menor que - el árbol usa esto para decidir si va a la izquierda"""
        if isinstance(other, Kid):
            return self.id < other.id
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Kid):
            return self.id <= other.id
        return NotImplemented
    
    def __gt__(self, other):
        """Mayor que - el árbol usa esto para decidir si va a la derecha"""
        if isinstance(other, Kid):
            return self.id > other.id
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Kid):
            return self.id >= other.id
        return NotImplemented
