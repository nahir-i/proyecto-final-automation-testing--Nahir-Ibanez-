import requests
import pytest
from datetime import datetime
from conftest import logger
from faker import Faker


# Configuración API y Faker
BASE_URL = "https://jsonplaceholder.typicode.com"
fake= Faker()

# Creación de la clase para testear las peticiones a la API
class TestJSONPlaceholder:
    
    # TEST 1: GET - Obtener todos los posts (Éxito)
    def test_get_posts_success(self):
        logger.info("\n=== Test 1: GET Posts ===")
        
        # Hacer petición GET
        response = requests.get(f"{BASE_URL}/posts")
        
        # Validar código de estado
        assert response.status_code == 200, f"Esperado 200, Obtenido {response.status_code}"
        logger.info(f"Petición GET /posts. Status: {response.status_code} OK")
        
        # Convertir a JSON
        data = response.json()
        
        # Validar estructura del JSON
        assert isinstance(data, list), "La respuesta debería ser una lista"
        assert len(data) > 0, "La lista no debería estar vacía"
        logger.info("Estructura JSON correcta")
        
        # Validar estructura
        first_post = data[0]
        required_fields = ["userId", "id", "title", "body"]
        for field in required_fields:
            assert field in first_post, f"Campo '{field}' no encontrado"
        logger.info("Test GET Posts completado exitosamente!")

        # Validar tipos de datos
        assert isinstance(first_post["id"], int)
        assert isinstance(first_post["title"], str)
        assert isinstance(first_post["body"], str)
        logger.info("Tipos de datos correctos")
        
    
    # TEST 2: POST - Crear un nuevo post (Éxito)
    def test_create_post_success(self):
        logger.info("\n=== Test 2: CREATE Post ===")
        
        # Creación de datos para crear el post
        post_data = {
            "title": fake.word(),
            "body": fake.text(),
            "userId": fake.random_int(1,6)
        }
        
        # Hacer petición POST
        response = requests.post(f"{BASE_URL}/posts", json=post_data)
        
        # Validar código de estado
        assert response.status_code == 201, f"Esperado 201, obtenido {response.status_code}"
        logger.info("Código de estado 201 - Created")
        
        # Convertir a JSON
        data = response.json()
        
        # Validar estructura de respuesta
        expected_fields = ["id", "title", "body", "userId"]
        for field in expected_fields:
            assert field in data, f"Campo '{field}' no encontrado en respuesta"
        logger.info("Estructura de respuesta correcta")
        
        # Validar que los datos se guardaron correctamente
        assert data["title"] == post_data["title"]
        assert data["body"] == post_data["body"]
        assert data["userId"] == post_data["userId"]
        logger.info("Datos guardados correctamente")
        
        # Validar que se asignó un ID (simulado por JSONPlaceholder)
        assert data["id"] == 101, f"Expected ID 101, got {data['id']}"
        logger.info("ID asignado correctamente")
        
        logger.info("Test CREATE Post completado exitosamente!")
    
    # TEST 3: DELETE - Eliminar un post (Éxito)
    def test_delete_post_success(self):
        logger.info("\n=== Test 3: DELETE Post ===")
        
        # ID del post a eliminar
        post_id = 1
        
        # Hacer petición DELETE
        response = requests.delete(f"{BASE_URL}/posts/{post_id}")
        
        # Validar código de estado
        assert response.status_code == 200, f"Esperado 200, obtenido {response.status_code}"
        logger.info("Código de estado 200 - OK")
        
        data = response.json()
        assert data == {}, f"Esperado un diccionario vacio, obtenido {data}"
        logger.info("Respuesta DELETE correcta")
        
        logger.info("Test DELETE Post completado exitosamente!")
