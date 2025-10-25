"""Script de prueba para la funcionalidad kidsbygroupedages"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_kids_by_grouped_ages():
    print("=" * 70)
    print("PRUEBA DE KIDSBYGROUPEDAGES - AGRUPAR KIDS POR RANGOS DE EDAD")
    print("=" * 70)
    
    # Limpiar el árbol
    print("\n1. Limpiando el árbol...")
    response = requests.delete(f"{BASE_URL}/tree/clear")
    print(f"   ✅ {response.json()['message']}")
    
    # Insertar Kids con diferentes edades
    print("\n2. Insertando Kids con diferentes edades:")
    kids_data = [
        {"kid_id": 10, "name": "Laura", "age": 2},
        {"kid_id": 20, "name": "Ana", "age": 3},
        {"kid_id": 25, "name": "Carlos", "age": 3},
        {"kid_id": 30, "name": "María", "age": 5},
        {"kid_id": 35, "name": "Diego", "age": 6},
        {"kid_id": 40, "name": "Luis", "age": 8},
        {"kid_id": 45, "name": "Elena", "age": 9},
        {"kid_id": 50, "name": "Juan", "age": 10},
        {"kid_id": 60, "name": "Sofía", "age": 11},
        {"kid_id": 70, "name": "Pedro", "age": 12},
        {"kid_id": 75, "name": "Lucía", "age": 12},
        {"kid_id": 80, "name": "Miguel", "age": 14},
    ]
    
    for kid_data in kids_data:
        response = requests.post(f"{BASE_URL}/tree/insert", params=kid_data)
        result = response.json()
        status = "✅" if result.get('success') else "❌"
        kid = result['data']['kid']
        print(f"   {status} Kid(id={kid['id']}, name='{kid['name']}', age={kid['age']})")
    
    # Tabla de Kids insertados
    print("\n3. Tabla completa de Kids en el árbol:")
    print("   " + "-" * 50)
    print(f"   {'ID':<6} {'Nombre':<15} {'Edad':<6}")
    print("   " + "-" * 50)
    for kid_data in sorted(kids_data, key=lambda x: x['age']):
        print(f"   {kid_data['kid_id']:<6} {kid_data['name']:<15} {kid_data['age']:<6}")
    print("   " + "-" * 50)
    
    # Probar con diferentes tamaños de rango
    print("\n4. Agrupando Kids por diferentes rangos de edad:")
    
    test_ranges = [3, 5, 4]
    
    for range_size in test_ranges:
        print(f"\n   📊 Agrupando con rangos de tamaño {range_size}:")
        response = requests.post(f"{BASE_URL}/tree/kidsbygroupedages", params={"range_size": range_size})
        result = response.json()
        
        if result.get('success'):
            data = result['data']
            print(f"   ✅ {result['message']}")
            print(f"   Total de Kids: {data['total_kids']}")
            print(f"\n   📋 Distribución por rangos:")
            print("   " + "-" * 40)
            print(f"   {'Rango':<15} {'Cantidad':<10}")
            print("   " + "-" * 40)
            
            for range_info in data['ranges']:
                print(f"   {range_info['range']:<15} {range_info['quantity']:<10}")
            
            print("   " + "-" * 40)
    
    # Caso práctico: Dividir en 3 grupos
    print("\n5. Caso práctico - Dividir Kids en grupos de 3 años:")
    response = requests.post(f"{BASE_URL}/tree/kidsbygroupedages", params={"range_size": 3})
    result = response.json()
    
    if result.get('success'):
        data = result['data']
        print(f"   Total de Kids: {data['total_kids']}")
        print(f"\n   📊 Gráfico visual:")
        for range_info in data['ranges']:
            bar = "█" * range_info['quantity']
            print(f"   {range_info['range']:<10} | {bar} ({range_info['quantity']})")
    
    # Caso especial: rango de 1 (cada edad por separado)
    print("\n6. Caso especial - Rango de 1 año (cada edad por separado):")
    response = requests.post(f"{BASE_URL}/tree/kidsbygroupedages", params={"range_size": 1})
    result = response.json()
    
    if result.get('success'):
        data = result['data']
        print(f"   Total de Kids: {data['total_kids']}")
        print(f"\n   📋 Distribución detallada:")
        print("   " + "-" * 40)
        for range_info in data['ranges']:
            bar = "●" * range_info['quantity']
            print(f"   Edad {range_info['range']:<8} | {bar} ({range_info['quantity']})")
        print("   " + "-" * 40)
    
    # Validación: rango inválido
    print("\n7. Validación - Intentar con rango inválido (0):")
    response = requests.post(f"{BASE_URL}/tree/kidsbygroupedages", params={"range_size": 0})
    result = response.json()
    if not result.get('success'):
        print(f"   ❌ {result['message']}")
        print(f"   ✅ Validación funcionando correctamente")
    
    print("\n" + "=" * 70)
    print("✅ PRUEBAS COMPLETADAS")
    print("=" * 70)
    print("\n📋 RESUMEN DE LA FUNCIONALIDAD:")
    print("   • Endpoint: POST /tree/kidsbygroupedages?range_size=X")
    print("   • Parámetro: range_size (tamaño del rango)")
    print("   • Devuelve: Lista de rangos con cantidad de Kids")
    print("   • Formato: [{'range': '0-3', 'quantity': 4}, ...]")
    print("\n📖 EJEMPLOS:")
    print("   • range_size=3 → Rangos: 0-3, 4-6, 7-9, 10-12, etc.")
    print("   • range_size=5 → Rangos: 0-5, 6-10, 11-15, etc.")
    print("   • range_size=1 → Cada edad por separado")
    print("=" * 70)

if __name__ == "__main__":
    try:
        test_kids_by_grouped_ages()
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar al servidor.")
        print("   Asegúrate de que el servidor esté corriendo en http://localhost:8000")
    except Exception as e:
        print(f"❌ Error durante las pruebas: {e}")
        import traceback
        traceback.print_exc()
