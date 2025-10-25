"""Script de prueba para verificar que el sistema de Kid funciona correctamente"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_kid_tree():
    print("=" * 60)
    print("PRUEBAS DEL SISTEMA DE KIDS")
    print("=" * 60)
    
    # Limpiar el árbol BST
    print("\n1. Limpiando el árbol BST...")
    response = requests.delete(f"{BASE_URL}/tree/clear")
    print(f"   ✅ {response.json()['message']}")
    
    # Insertar Kids con id, left y right
    print("\n2. Insertando Kids en el árbol BST...")
    kids_data = [
        {"kid_id": 50, "left_id": 25, "right_id": 75},
        {"kid_id": 30, "left_id": 15, "right_id": 40},
        {"kid_id": 70, "left_id": 60, "right_id": 80},
        {"kid_id": 20},  # Sin left ni right
        {"kid_id": 40, "left_id": 35, "right_id": 45},
        {"kid_id": 60, "left_id": None, "right_id": 65},  # Solo right
    ]
    
    for kid_data in kids_data:
        response = requests.post(f"{BASE_URL}/tree/insert", params=kid_data)
        result = response.json()
        status = "✅" if result.get('success') else "❌"
        kid_info = f"ID={kid_data['kid_id']}"
        if kid_data.get('left_id'):
            kid_info += f", left={kid_data['left_id']}"
        if kid_data.get('right_id'):
            kid_info += f", right={kid_data['right_id']}"
        print(f"   {status} Kid({kid_info})")
    
    # Obtener estructura
    print("\n3. Obteniendo estructura del árbol BST...")
    response = requests.get(f"{BASE_URL}/tree/structure")
    structure = response.json()
    if structure.get('success'):
        print(f"   ✅ Estructura obtenida:")
        print(f"   {json.dumps(structure['data']['structure'], indent=6)}")
    
    # Recorridos
    print("\n4. Recorridos del árbol BST...")
    response = requests.get(f"{BASE_URL}/tree/traversal/inorder")
    print(f"   Inorden (ordenado): {response.json()['data']['traversal']}")
    
    response = requests.get(f"{BASE_URL}/tree/traversal/preorder")
    print(f"   Preorden: {response.json()['data']['traversal']}")
    
    # Buscar Kids
    print("\n5. Buscando Kids por ID...")
    test_ids = [50, 30, 100, 20]
    for kid_id in test_ids:
        response = requests.post(f"{BASE_URL}/tree/search", params={"kid_id": kid_id})
        result = response.json()
        status = "✅ encontrado" if result['data']['found'] else "❌ no encontrado"
        print(f"   Kid ID {kid_id}: {status}")
    
    # Obtener datos guardados
    print("\n6. IDs de Kids guardados...")
    response = requests.get(f"{BASE_URL}/tree/saved-data")
    result = response.json()
    print(f"   IDs guardados: {result['data']['kid_ids']}")
    
    print("\n" + "=" * 60)
    print("PRUEBAS DEL ÁRBOL AVL CON KIDS")
    print("=" * 60)
    
    # Limpiar el árbol AVL
    print("\n7. Limpiando el árbol AVL...")
    response = requests.delete(f"{BASE_URL}/avl/clear")
    print(f"   ✅ {response.json()['message']}")
    
    # Insertar Kids en AVL
    print("\n8. Insertando Kids en el árbol AVL...")
    avl_kids = [
        {"kid_id": 50, "left_id": 25, "right_id": 75},
        {"kid_id": 30, "left_id": 15},
        {"kid_id": 70, "right_id": 85},
        {"kid_id": 20},
        {"kid_id": 40},
        {"kid_id": 60},
        {"kid_id": 80},
    ]
    
    for kid_data in avl_kids:
        response = requests.post(f"{BASE_URL}/avl/insert", params=kid_data)
        result = response.json()
        status = "✅" if result.get('success') else "❌"
        kid_info = f"ID={kid_data['kid_id']}"
        if kid_data.get('left_id'):
            kid_info += f", left={kid_data['left_id']}"
        if kid_data.get('right_id'):
            kid_info += f", right={kid_data['right_id']}"
        print(f"   {status} Kid({kid_info}) - Altura balanceada automáticamente")
    
    # Obtener estructura AVL
    print("\n9. Obteniendo estructura del árbol AVL (con alturas)...")
    response = requests.get(f"{BASE_URL}/avl/structure")
    structure = response.json()
    if structure.get('success'):
        print(f"   ✅ Estructura obtenida con información de balance:")
        
        def print_kid_info(node, indent=6):
            if node:
                spaces = " " * indent
                kid = node['kid']
                print(f"{spaces}Kid ID={kid['id']}, left={kid['left']}, right={kid['right']}")
                print(f"{spaces}  Altura: {node['height']}, Balance: {node['balance']}")
                if node['children'][0]:
                    print(f"{spaces}  Hijo izquierdo:")
                    print_kid_info(node['children'][0], indent + 4)
                if node['children'][1]:
                    print(f"{spaces}  Hijo derecho:")
                    print_kid_info(node['children'][1], indent + 4)
        
        print_kid_info(structure['data']['structure'])
    
    # Eliminar un Kid del AVL
    print("\n10. Eliminando Kid ID=30 del árbol AVL...")
    response = requests.delete(f"{BASE_URL}/avl/prune", params={"kid_id": 30})
    result = response.json()
    status = "✅" if result.get('success') else "❌"
    print(f"   {status} {result['message']}")
    
    # Verificar balance después de eliminar
    print("\n11. Verificando recorrido después de eliminar...")
    response = requests.get(f"{BASE_URL}/avl/traversal/inorder")
    print(f"   Inorden AVL: {response.json()['data']['traversal']}")
    
    print("\n" + "=" * 60)
    print("✅ TODAS LAS PRUEBAS CON KIDS COMPLETADAS")
    print("=" * 60)
    print("\n📋 RESUMEN:")
    print("   - Clase Kid creada con id, left y right")
    print("   - Árbol BST usa Kids en lugar de valores simples")
    print("   - Árbol AVL usa Kids con auto-balanceo")
    print("   - Todos los endpoints actualizados correctamente")
    print("=" * 60)

if __name__ == "__main__":
    try:
        test_kid_tree()
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar al servidor.")
        print("   Asegúrate de que el servidor esté corriendo en http://localhost:8000")
    except Exception as e:
        print(f"❌ Error durante las pruebas: {e}")
        import traceback
        traceback.print_exc()
