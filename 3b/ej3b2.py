"""
Enunciado:
Desarrolla una API REST utilizando Flask que permita realizar operaciones básicas sobre una biblioteca
con dos modelos relacionados: Autores y Libros.
La API debe exponer los siguientes endpoints:

Autores:
1. `GET /authors`: Devuelve la lista completa de autores.
2. `POST /authors`: Agrega un nuevo autor. El cuerpo de la solicitud debe incluir un JSON con el campo "name".
3. `GET /authors/<author_id>`: Obtiene los detalles de un autor específico y su lista de libros.

Libros:
1. `GET /books`: Devuelve la lista completa de libros.
2. `POST /books`: Agrega un nuevo libro. El cuerpo de la solicitud debe incluir JSON con campos "title", "author_id", y "year" (opcional).
3. `DELETE /books/<book_id>`: Elimina un libro específico por su ID.
4. `PUT /books/<book_id>`: Actualiza la información de un libro existente. El cuerpo puede incluir "title" y/o "year".

Esta versión utiliza Flask-SQLAlchemy como ORM para persistir los datos en una base de datos SQLite.
"""

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define aquí tus modelos
# Usa los mismos modelos que en el ejercicio anterior: Author y Book

class Author(db.Model):
    """
    Modelo de autor usando SQLAlchemy ORM
    Debe tener: id, name y una relación con los libros
    """
    # Define la tabla 'authors' con:
    # - __tablename__ para especificar el nombre de la tabla
    # - id: clave primaria autoincremental
    # - name: nombre del autor (obligatorio)
    # - Una relación con los libros usando db.relationship
    pass

    def to_dict(self):
        """Convierte el autor a un diccionario para la respuesta JSON"""
        # Implementa este método para devolver id y name
        # No incluyas la lista de libros para evitar recursión infinita
        pass


class Book(db.Model):
    """
    Modelo de libro usando SQLAlchemy ORM
    Debe tener: id, title, year (opcional), author_id y relación con el autor
    """
    # Define la tabla 'books' con:
    # - __tablename__ para especificar el nombre de la tabla
    # - id: clave primaria autoincremental
    # - title: título del libro (obligatorio)
    # - year: año de publicación (opcional)
    # - author_id: clave foránea que relaciona con la tabla 'authors'
    pass

    def to_dict(self):
        """Convierte el libro a un diccionario para la respuesta JSON"""
        # Implementa este método para devolver id, title, year y author_id
        pass


def create_app():
    """
    Crea y configura la aplicación Flask con SQLAlchemy
    """
    app = Flask(__name__)
    
    # Configuración de la base de datos SQLite en memoria
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializa la base de datos con la aplicación
    db.init_app(app)
    
    # Crea todas las tablas en la base de datos
    with app.app_context():
        db.create_all()
    
    # Endpoints de Autores
    @app.route('/authors', methods=['GET'])
    def get_authors():
        """
        Devuelve la lista completa de autores
        """
        # Implementa este endpoint:
        # - Consulta todos los autores
        # - Convierte cada autor a diccionario usando to_dict()
        # - Devuelve la lista en formato JSON
        pass

    @app.route('/authors', methods=['POST'])
    def add_author():
        """
        Agrega un nuevo autor
        El cuerpo de la solicitud debe incluir un JSON con el campo "name"
        """
        # Implementa este endpoint:
        # - Obtiene los datos JSON de la solicitud
        # - Crea un nuevo autor con el nombre proporcionado
        # - Lo guarda en la base de datos
        # - Devuelve el autor creado con código 201
        pass

    @app.route('/authors/<int:author_id>', methods=['GET'])
    def get_author(author_id):
        """
        Obtiene los detalles de un autor específico y su lista de libros
        """
        # Implementa este endpoint:
        # - Busca el autor por ID (usa get_or_404 para gestionar el error 404)
        # - Devuelve los detalles del autor y su lista de libros
        pass

    # Endpoints de Libros
    @app.route('/books', methods=['GET'])
    def get_books():
        """
        Devuelve la lista completa de libros
        """
        # Implementa este endpoint:
        # - Consulta todos los libros
        # - Convierte cada libro a diccionario
        # - Devuelve la lista en formato JSON
        pass

    @app.route('/books', methods=['POST'])
    def add_book():
        """
        Agrega un nuevo libro
        El cuerpo de la solicitud debe incluir JSON con campos "title", "author_id", y "year" (opcional)
        """
        # Implementa este endpoint:
        # - Obtiene los datos JSON de la solicitud
        # - Crea un nuevo libro con título, autor_id y año (opcional)
        # - Lo guarda en la base de datos
        # - Devuelve el libro creado con código 201
        pass

    @app.route('/books/<int:book_id>', methods=['GET'])
    def get_book(book_id):
        """
        Obtiene un libro específico por su ID
        """
        # Implementa este endpoint:
        # - Busca el libro por ID (usa get_or_404 para gestionar el error 404)
        # - Devuelve los detalles del libro
        pass

    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        """
        Elimina un libro específico por su ID
        """
        # Implementa este endpoint:
        # - Busca el libro por ID (usa get_or_404)
        # - Elimina el libro de la base de datos
        # - Devuelve respuesta vacía con código 204
        pass

    @app.route('/books/<int:book_id>', methods=['PUT'])
    def update_book(book_id):
        """
        Actualiza la información de un libro existente
        El cuerpo puede incluir "title" y/o "year"
        """
        # Implementa este endpoint:
        # - Obtiene los datos JSON de la solicitud
        # - Busca el libro por ID (usa get_or_404)
        # - Actualiza los campos proporcionados (título y/o año)
        # - Guarda los cambios en la base de datos
        # - Devuelve el libro actualizado
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
