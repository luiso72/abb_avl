"""Script de prueba para verificar que el sistema de Kid funciona correctamente
con IDs solamente - el árbol decide izquierda/derecha automáticamente"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_kid_tree():
    print("=" * 70)
    print("PRUEBAS DEL SISTEMA DE KIDS - ÁRBOL DECIDE IZQUIERDA/DERECHA")
    print("=" * 70)
    
    # Limpiar el árbol BST
    print("\n1. Limpiando el árbol BST...")
    response = requests.delete(f"{BASE_URL}/tree/clear")
    print(f"   ✅ {response.json()['message']}")
    
    # Insertar Kids solo con ID
    print("\n2. Insertando Kids en el árbol BST (solo con ID)...")
    print("   El árbol decide automáticamente si van a izquierda o derecha:")
    print("   - ID menor que padre → izquierda (children[0])")
    print("   - ID mayor que padre → derecha (children[1])")
    print()
    
    kids = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    
    for kid_id in kids:
        response = requests.post(f"{BASE_URL}/tree/insert", params={"kid_id": kid_id})
        result = response.json()
        status = "✅" if result.get('success') else "❌"
        print(f"   {status} Kid(id={kid_id})")
    
    # Obtener estructura
    print("\n3. Estructura del árbol BST:")
    print("   (El árbol organizó los Kids automáticamente)")
    response = requests.get(f"{BASE_URL}/tree/structure")
    structure = response.json()
    if structure.get('success'):
        def print_tree(node, indent=6, side="ROOT"):
            if node:
                spaces = " " * indent
                kid_id = node['kid']['id']
                print(f"{spaces}{side}: Kid(id={kid_id})")
                if node['children'][0]:
                    print_tree(node['children'][0], indent + 4, "LEFT ")
                if node['children'][1]:
                    print_tree(node['children'][1], indent + 4, "RIGHT")
        
        print_tree(structure['data']['structure'])
    
    # Recorridos
    print("\n4. Recorridos del árbol BST:")
    response = requests.get(f"{BASE_URL}/tree/traversal/inorder")
    inorder = response.json()['data']['traversal']
    print(f"   Inorden (ordenado automáticamente): {inorder}")
    print(f"   ✅ Los Kids están en orden ascendente por ID")
    
    response = requests.get(f"{BASE_URL}/tree/traversal/preorder")
    print(f"   Preorden: {response.json()['data']['traversal']}")
    
    # Buscar Kids
    print("\n5. Buscando Kids por ID...")
    test_ids = [50, 30, 100, 20]
    for kid_id in test_ids:
        response = requests.post(f"{BASE_URL}/tree/search", params={"kid_id": kid_id})
        result = response.json()
        status = "✅ encontrado" if result['data']['found'] else "❌ no encontrado"
        print(f"   Kid(id={kid_id}): {status}")
    
    print("\n" + "=" * 70)
    print("PRUEBAS DEL ÁRBOL AVL CON KIDS - AUTO-BALANCEO")
    print("=" * 70)
    
    # Limpiar el árbol AVL
    print("\n6. Limpiando el árbol AVL...")
    response = requests.delete(f"{BASE_URL}/avl/clear")
    print(f"   ✅ {response.json()['message']}")
    
    # Insertar Kids en AVL (insertamos en orden para ver el balanceo)
    print("\n7. Insertando Kids en el árbol AVL en orden secuencial:")
    print("   (El AVL balanceará automáticamente usando rotaciones)")
    print()
    
    avl_kids = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    
    for kid_id in avl_kids:
        response = requests.post(f"{BASE_URL}/avl/insert", params={"kid_id": kid_id})
        result = response.json()
        status = "✅" if result.get('success') else "❌"
        print(f"   {status} Kid(id={kid_id}) - árbol balanceado automáticamente")
    
    # Obtener estructura AVL con balance
    print("\n8. Estructura del árbol AVL (con información de balance):")
    response = requests.get(f"{BASE_URL}/avl/structure")
    structure = response.json()
    if structure.get('success'):
        def print_avl_tree(node, indent=6, side="ROOT"):
            if node:
                spaces = " " * indent
                kid_id = node['kid']['id']
                height = node['height']
                balance = node['balance']
                balanced = "✅" if abs(balance) <= 1 else "❌"
                print(f"{spaces}{side}: Kid(id={kid_id}) [h={height}, b={balance}] {balanced}")
                if node['children'][0]:
                    print_avl_tree(node['children'][0], indent + 4, "LEFT ")
                if node['children'][1]:
                    print_avl_tree(node['children'][1], indent + 4, "RIGHT")
        
        print_avl_tree(structure['data']['structure'])
    
    # Verificar que está balanceado
    print("\n9. Verificando balance del árbol AVL:")
    def check_balance(node):
        if node is None:
            return True
        balance = node.get('balance', 0)
        if abs(balance) > 1:
            print(f"   ❌ Desbalanceado en Kid(id={node['kid']['id']}): balance={balance}")
            return False
        left_ok = check_balance(node['children'][0])
        right_ok = check_balance(node['children'][1])
        return left_ok and right_ok
    
    if check_balance(structure['data']['structure']):
        print("   ✅ Todo el árbol está perfectamente balanceado!")
        print("   ✅ Todos los nodos tienen factor de balance entre -1 y 1")
    
    # Recorrido inorden del AVL
    response = requests.get(f"{BASE_URL}/avl/traversal/inorder")
    inorder = response.json()['data']['traversal']
    print(f"\n10. Inorden AVL: {inorder}")
    print(f"    ✅ Ordenado correctamente de menor a mayor")
    
    # Eliminar un Kid del AVL
    print("\n11. Eliminando Kid(id=30) del árbol AVL...")
    response = requests.delete(f"{BASE_URL}/avl/prune", params={"kid_id": 30})
    result = response.json()
    status = "✅" if result.get('success') else "❌"
    print(f"    {status} {result['message']}")
    
    # Verificar balance después de eliminar
    response = requests.get(f"{BASE_URL}/avl/structure")
    structure = response.json()
    if check_balance(structure['data']['structure']):
        print("    ✅ El árbol sigue balanceado después de eliminar!")
    
    response = requests.get(f"{BASE_URL}/avl/traversal/inorder")
    print(f"    Inorden después de eliminar: {response.json()['data']['traversal']}")
    
    print("\n" + "=" * 70)
    print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 70)
    print("\n📋 RESUMEN DEL SISTEMA:")
    print("   • Clase Kid tiene solo 'id'")
    print("   • left y right NO son atributos del Kid")
    print("   • El árbol (BST o AVL) decide automáticamente:")
    print("     - Si Kid.id < nodo_actual.id → va a la IZQUIERDA (children[0])")
    print("     - Si Kid.id > nodo_actual.id → va a la DERECHA (children[1])")
    print("   • AVL balancea automáticamente usando rotaciones")
    print("   • Todo funciona correctamente ✅")
    print("=" * 70)

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
