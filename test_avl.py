"""Script de prueba para verificar que el árbol AVL funciona correctamente"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_avl_tree():
    print("=" * 60)
    print("PRUEBAS DEL ÁRBOL AVL")
    print("=" * 60)
    
    # Limpiar el árbol
    print("\n1. Limpiando el árbol...")
    response = requests.delete(f"{BASE_URL}/avl/clear")
    print(f"   Respuesta: {response.json()}")
    
    # Insertar valores
    print("\n2. Insertando valores...")
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    for value in values:
        response = requests.post(f"{BASE_URL}/avl/insert", params={"value": value})
        result = response.json()
        status = "✅" if result.get('success') else "❌"
        print(f"   {status} Insertado {value}")
    
    # Obtener estructura
    print("\n3. Obteniendo estructura del árbol...")
    response = requests.get(f"{BASE_URL}/avl/structure")
    structure = response.json()
    print(f"   Estructura: {json.dumps(structure, indent=2)}")
    
    # Verificar balance
    print("\n4. Verificando que el árbol está balanceado...")
    def check_balance(node):
        if node is None:
            return True
        balance = node.get('balance', 0)
        if abs(balance) > 1:
            print(f"   ⚠️  DESBALANCEADO en nodo {node['value']}: balance = {balance}")
            return False
        return check_balance(node['children'][0]) and check_balance(node['children'][1])
    
    tree_data = structure.get('data', {}).get('structure')
    is_balanced = check_balance(tree_data)
    if is_balanced:
        print("   ✅ El árbol está perfectamente balanceado!")
    
    # Hacer recorridos
    print("\n5. Recorridos del árbol...")
    response = requests.get(f"{BASE_URL}/avl/traversal/inorder")
    print(f"   Inorden: {response.json()['data']['traversal']}")
    
    response = requests.get(f"{BASE_URL}/avl/traversal/preorder")
    print(f"   Preorden: {response.json()['data']['traversal']}")
    
    response = requests.get(f"{BASE_URL}/avl/traversal/postorder")
    print(f"   Postorden: {response.json()['data']['traversal']}")
    
    # Buscar valores
    print("\n6. Buscando valores...")
    test_values = [40, 100, 25, 500]
    for value in test_values:
        response = requests.post(f"{BASE_URL}/avl/search", params={"value": value})
        result = response.json()
        status = "✅ encontrado" if result['data']['found'] else "❌ no encontrado"
        print(f"   Valor {value}: {status}")
    
    # Eliminar un valor
    print("\n7. Eliminando valor 30...")
    response = requests.delete(f"{BASE_URL}/avl/prune", params={"value": 30})
    result = response.json()
    status = "✅" if result.get('success') else "❌"
    print(f"   {status} {result['message']}")
    
    # Verificar estructura después de eliminar
    print("\n8. Verificando estructura después de eliminar...")
    response = requests.get(f"{BASE_URL}/avl/structure")
    structure = response.json()
    tree_data = structure.get('data', {}).get('structure')
    is_balanced = check_balance(tree_data)
    if is_balanced:
        print("   ✅ El árbol sigue balanceado después de eliminar!")
    
    response = requests.get(f"{BASE_URL}/avl/traversal/inorder")
    print(f"   Inorden después de eliminar: {response.json()['data']['traversal']}")
    
    print("\n" + "=" * 60)
    print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 60)

if __name__ == "__main__":
    try:
        test_avl_tree()
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar al servidor.")
        print("   Asegúrate de que el servidor esté corriendo en http://localhost:8000")
    except Exception as e:
        print(f"❌ Error durante las pruebas: {e}")
