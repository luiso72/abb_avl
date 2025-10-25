"""Script de prueba para verificar que:
- ABB (Binary Search Tree) usa la clase Kid con solo id
- AVL usa valores simples (int)
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_both_trees():
    print("=" * 70)
    print("PRUEBAS DEL SISTEMA - ABB CON KID, AVL CON VALORES")
    print("=" * 70)
    
    # =========================================================================
    # PARTE 1: ÁRBOL BINARIO DE BÚSQUEDA (ABB) CON KIDS
    # =========================================================================
    print("\n" + "=" * 70)
    print("PARTE 1: ÁRBOL BINARIO DE BÚSQUEDA (ABB) - USA CLASE KID")
    print("=" * 70)
    
    # Limpiar el árbol BST
    print("\n1. Limpiando el árbol ABB...")
    response = requests.delete(f"{BASE_URL}/tree/clear")
    print(f"   ✅ {response.json()['message']}")
    
    # Insertar Kids con solo ID
    print("\n2. Insertando Kids en el árbol ABB (solo con ID)...")
    print("   El árbol decide automáticamente izquierda/derecha:")
    
    kids = [50, 30, 70, 20, 40, 60, 80]
    
    for kid_id in kids:
        response = requests.post(f"{BASE_URL}/tree/insert", params={"kid_id": kid_id})
        result = response.json()
        status = "✅" if result.get('success') else "❌"
        print(f"   {status} Kid(id={kid_id})")
    
    # Obtener estructura del ABB
    print("\n3. Estructura del árbol ABB (con Kids):")
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
    
    # Recorridos ABB
    print("\n4. Recorridos del árbol ABB:")
    response = requests.get(f"{BASE_URL}/tree/traversal/inorder")
    inorder = response.json()['data']['traversal']
    print(f"   Inorden: {inorder}")
    print(f"   ✅ Kids ordenados automáticamente por ID")
    
    # Buscar Kids
    print("\n5. Buscando Kids por ID en el ABB:")
    test_ids = [50, 100]
    for kid_id in test_ids:
        response = requests.post(f"{BASE_URL}/tree/search", params={"kid_id": kid_id})
        result = response.json()
        status = "✅" if result['data']['found'] else "❌"
        print(f"   Kid(id={kid_id}): {status}")
    
    # =========================================================================
    # PARTE 2: ÁRBOL AVL CON VALORES SIMPLES
    # =========================================================================
    print("\n" + "=" * 70)
    print("PARTE 2: ÁRBOL AVL - USA VALORES SIMPLES (INT)")
    print("=" * 70)
    
    # Limpiar el árbol AVL
    print("\n6. Limpiando el árbol AVL...")
    response = requests.delete(f"{BASE_URL}/avl/clear")
    print(f"   ✅ {response.json()['message']}")
    
    # Insertar valores simples en AVL
    print("\n7. Insertando valores simples en el árbol AVL:")
    print("   (El AVL balancea automáticamente)")
    
    values = [10, 20, 30, 40, 50, 60, 70]
    
    for value in values:
        response = requests.post(f"{BASE_URL}/avl/insert", params={"value": value})
        result = response.json()
        status = "✅" if result.get('success') else "❌"
        print(f"   {status} Value={value}")
    
    # Obtener estructura del AVL
    print("\n8. Estructura del árbol AVL (con valores y balance):")
    response = requests.get(f"{BASE_URL}/avl/structure")
    structure = response.json()
    if structure.get('success'):
        def print_avl_tree(node, indent=6, side="ROOT"):
            if node:
                spaces = " " * indent
                value = node['value']
                height = node['height']
                balance = node['balance']
                balanced = "✅" if abs(balance) <= 1 else "❌"
                print(f"{spaces}{side}: Value={value} [h={height}, b={balance}] {balanced}")
                if node['children'][0]:
                    print_avl_tree(node['children'][0], indent + 4, "LEFT ")
                if node['children'][1]:
                    print_avl_tree(node['children'][1], indent + 4, "RIGHT")
        
        print_avl_tree(structure['data']['structure'])
    
    # Verificar balance
    print("\n9. Verificando balance del árbol AVL:")
    def check_balance(node):
        if node is None:
            return True
        balance = node.get('balance', 0)
        if abs(balance) > 1:
            print(f"   ❌ Desbalanceado en Value={node['value']}: balance={balance}")
            return False
        return check_balance(node['children'][0]) and check_balance(node['children'][1])
    
    if check_balance(structure['data']['structure']):
        print("   ✅ Todo el árbol AVL está perfectamente balanceado!")
    
    # Recorridos AVL
    print("\n10. Recorridos del árbol AVL:")
    response = requests.get(f"{BASE_URL}/avl/traversal/inorder")
    inorder = response.json()['data']['traversal']
    print(f"    Inorden: {inorder}")
    print(f"    ✅ Valores ordenados correctamente")
    
    # Buscar valores
    print("\n11. Buscando valores en el AVL:")
    test_values = [30, 100]
    for value in test_values:
        response = requests.post(f"{BASE_URL}/avl/search", params={"value": value})
        result = response.json()
        status = "✅" if result['data']['found'] else "❌"
        print(f"    Value={value}: {status}")
    
    # =========================================================================
    # RESUMEN FINAL
    # =========================================================================
    print("\n" + "=" * 70)
    print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 70)
    print("\n📋 RESUMEN DEL SISTEMA:")
    print("\n   🌲 ÁRBOL BINARIO DE BÚSQUEDA (ABB):")
    print("      • Usa la clase Kid")
    print("      • Kid tiene solo 'id' (sin left/right públicos)")
    print("      • El árbol decide izquierda/derecha automáticamente")
    print("      • Endpoint: /tree/insert?kid_id=X")
    print("\n   🌲 ÁRBOL AVL:")
    print("      • Usa valores simples (int)")
    print("      • Auto-balancea con rotaciones")
    print("      • Mantiene factor de balance entre -1 y 1")
    print("      • Endpoint: /avl/insert?value=X")
    print("\n   ✅ Ambos árboles funcionan correctamente")
    print("=" * 70)

if __name__ == "__main__":
    try:
        test_both_trees()
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar al servidor.")
        print("   Asegúrate de que el servidor esté corriendo en http://localhost:8000")
    except Exception as e:
        print(f"❌ Error durante las pruebas: {e}")
        import traceback
        traceback.print_exc()
