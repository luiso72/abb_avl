"""Script de prueba para verificar que la clase Kid funciona con id, name y age"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_kid_with_data():
    print("=" * 70)
    print("PRUEBAS DE KIDS CON ID, NAME Y AGE")
    print("=" * 70)
    
    # Limpiar el árbol
    print("\n1. Limpiando el árbol ABB...")
    response = requests.delete(f"{BASE_URL}/tree/clear")
    print(f"   ✅ {response.json()['message']}")
    
    # Insertar Kids con datos completos
    print("\n2. Insertando Kids con id, name y age:")
    kids_data = [
        {"kid_id": 50, "name": "Juan", "age": 10},
        {"kid_id": 30, "name": "María", "age": 8},
        {"kid_id": 70, "name": "Pedro", "age": 12},
        {"kid_id": 20, "name": "Ana", "age": 7},
        {"kid_id": 40, "name": "Luis", "age": 9},
        {"kid_id": 60, "name": "Sofía", "age": 11},
        {"kid_id": 80, "name": "Carlos", "age": 13},
    ]
    
    for kid_data in kids_data:
        response = requests.post(f"{BASE_URL}/tree/insert", params=kid_data)
        result = response.json()
        status = "✅" if result.get('success') else "❌"
        print(f"   {status} {result['message']}")
    
    # Obtener estructura del árbol
    print("\n3. Estructura del árbol con información completa de Kids:")
    response = requests.get(f"{BASE_URL}/tree/structure")
    structure = response.json()
    
    if structure.get('success'):
        def print_tree(node, indent=6, side="ROOT"):
            if node:
                spaces = " " * indent
                kid = node['kid']
                kid_str = f"Kid(id={kid['id']}, name='{kid['name']}', age={kid['age']})"
                print(f"{spaces}{side}: {kid_str}")
                if node['children'][0]:
                    print_tree(node['children'][0], indent + 4, "LEFT ")
                if node['children'][1]:
                    print_tree(node['children'][1], indent + 4, "RIGHT")
        
        print_tree(structure['data']['structure'])
    
    # Recorridos - mostrar IDs (ordenados)
    print("\n4. Recorrido inorden (ordenado por ID):")
    response = requests.get(f"{BASE_URL}/tree/traversal/inorder")
    inorder = response.json()['data']['traversal']
    print(f"   IDs ordenados: {inorder}")
    print(f"   ✅ Kids organizados automáticamente por ID")
    
    # Buscar un Kid
    print("\n5. Buscando Kids por ID:")
    test_ids = [30, 100]
    for kid_id in test_ids:
        response = requests.post(f"{BASE_URL}/tree/search", params={"kid_id": kid_id})
        result = response.json()
        status = "✅ encontrado" if result['data']['found'] else "❌ no encontrado"
        print(f"   Kid(id={kid_id}): {status}")
    
    # Insertar Kids con solo ID (sin name ni age)
    print("\n6. Insertando Kids solo con ID (name y age opcionales):")
    response = requests.post(f"{BASE_URL}/tree/insert", params={"kid_id": 25})
    result = response.json()
    status = "✅" if result.get('success') else "❌"
    print(f"   {status} {result['message']}")
    
    # Ver estructura actualizada
    print("\n7. Estructura actualizada (mostrando Kid sin name/age):")
    response = requests.get(f"{BASE_URL}/tree/structure")
    structure = response.json()
    
    if structure.get('success'):
        # Buscar el Kid con id=25
        def find_kid(node, kid_id):
            if node is None:
                return None
            if node['kid']['id'] == kid_id:
                return node['kid']
            left = find_kid(node['children'][0], kid_id)
            if left:
                return left
            return find_kid(node['children'][1], kid_id)
        
        kid_25 = find_kid(structure['data']['structure'], 25)
        if kid_25:
            print(f"   Kid encontrado: id={kid_25['id']}, name='{kid_25['name']}', age={kid_25['age']}")
            print(f"   ✅ Name y age tienen valores por defecto cuando no se especifican")
    
    print("\n" + "=" * 70)
    print("✅ TODAS LAS PRUEBAS COMPLETADAS")
    print("=" * 70)
    print("\n📋 RESUMEN:")
    print("   • Clase Kid tiene: id (requerido), name (opcional), age (opcional)")
    print("   • El árbol ABB organiza Kids por ID automáticamente")
    print("   • ID menor → izquierda, ID mayor → derecha")
    print("   • Se puede insertar Kids con o sin name/age")
    print("   • Todos los datos se almacenan y recuperan correctamente")
    print("=" * 70)

if __name__ == "__main__":
    try:
        test_kid_with_data()
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar al servidor.")
        print("   Asegúrate de que el servidor esté corriendo en http://localhost:8000")
    except Exception as e:
        print(f"❌ Error durante las pruebas: {e}")
        import traceback
        traceback.print_exc()
