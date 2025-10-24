# Especificaciones del Proyecto
tiene que tener scollfolding con model, service y controller, se usara FastApi, python 3.13, y no puedeser nada avanzado de mas alla de cuarto semestre de ingenieria
## Descripción General
Proyecto de Árbol Binario de Búsqueda con API REST. El proyecto usa scaffolding con model, service y controller, utiliza FastAPI y Python 3.13, y no debe ser nada avanzado más allá de cuarto semestre de ingeniería.

Crear un árbol binario que se pueda usar mediante API REST para insertar, buscar, eliminar, recorrer y mostrar la estructura del árbol.

## Requisitos Funcionales
ABB (Árbol Binario de Búsqueda)
- Insertar valores en el árbol
- Buscar valores en el árbol
- Eliminar valores del árbol (podar)
- Recorrer el árbol en tres órdenes: inorden, preorden y postorden
- Mostrar la estructura del árbol
- Guardar todos los datos que se insertan
AVL (Árbol de Altura Balanceada)
- Insertar valores en el árbol
- Buscar valores en el árbol
- Eliminar valores del árbol (podar)
- Balancear el árbol
- Mostrar la estructura del árbol
- Guardar todos los datos que se insertan
## Estructura del Proyecto
```
windsurf-project-3/
├── app/
│   ├── models/          # Modelo de datos (Node)
│   ├── services/        # Lógica del árbol binario
│   └── controllers/     # Endpoints de la API
├── main.py             # Archivo principal
└── requirements.txt    # Dependencias
```

## Tecnologías a Utilizar
- FastAPI
- Python 3.13
- Uvicorn (servidor)

## Endpoints de la API
Tres funciones principales:
1. **insert** - Insertar un número en el árbol
2. **search** - Buscar un número en el árbol
3. **prune** - Eliminar un nodo del árbol
4. **clear** - Eliminar todo el árbol (poda completa)

Endpoints adicionales:
- `/tree/structure` - Ver la estructura completa
- `/tree/traversal/inorder` - Recorrido inorden
- `/tree/traversal/preorder` - Recorrido preorden
- `/tree/traversal/postorder` - Recorrido postorden
- `/tree/saved-data` - Ver todos los datos guardados

## Modelos de Datos
El árbol ABB (Árbol Binario de Búsqueda) funciona así:
- Número menor a la raíz → va a la izquierda
- Número mayor a la raíz → va a la derecha

## Servicios
Organizar con:
- **Inorden** (izquierda → raíz → derecha)
- **Preorden** (raíz → izquierda → derecha)
- **Postorden** (izquierda → derecha → raíz)

También se deben guardar la información que entra.

## Notas Adicionales
- La raíz se llamará **root**
- Las hojas se llamarán **children** (array de 2 elementos [izquierdo, derecho])
- Tres funciones principales: **insert**, **search** y **podar** (eliminar)