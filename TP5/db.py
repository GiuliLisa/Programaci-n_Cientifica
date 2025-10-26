#Reinaldo Giulianna
#2025
#Programación Científica

import sqlite3 # Importo la librería sqlite3, que ya viene incluida en Python.

# Creo una consulta SQL para crear una tabla con sus columnas (a la base de datos "biblioteca")
def create_table():
    db = sqlite3.connect('biblioteca.db')
    query = """
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        anio_publicacion INTEGER NOT NULL,
        genero TEXT NOT NULL
    )
    """
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    db.close()
    print("Tabla 'libros' creada o verificada correctamente.")

#Función para insertar un libro a la tabla
def insert_book(titulo, autor, anio_publicacion, genero):
    db = sqlite3.connect('biblioteca.db')
    # Consulta SQL con los valores que se van a insertar
    query = """
    INSERT INTO libros (titulo, autor, anio_publicacion, genero)
    VALUES (?, ?, ?, ?)
    """
    cur = db.cursor()
    cur.execute(query, (titulo, autor, anio_publicacion, genero))
    db.commit()
    db.close()
    print("Libro insertado correctamente.")

#Función para obtener todos los libros
def get_all_books():
    db = sqlite3.connect('biblioteca.db')
    #Selecciono todos los campos de la tabla libros
    query = "SELECT * FROM libros"
    cur = db.cursor()
    cur.execute(query)
    libros = cur.fetchall()
    db.close()
    return libros

# Actualizar un libro por ID
def update_book(book_id, nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_genero):
    db = sqlite3.connect('biblioteca.db')
    query = "UPDATE libros SET titulo=?, autor=?, anio_publicacion=?, genero=? WHERE id=?"
    cur = db.cursor()
    cur.execute(query, (nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_genero, book_id))
    db.commit()
    db.close()
    print("Libro actualizado correctamente.")

# Eliminar un libro por ID
def delete_book(book_id):
    db = sqlite3.connect('biblioteca.db')
    query = "DELETE FROM libros WHERE id=?"
    cur = db.cursor()
    cur.execute(query, (book_id,))
    db.commit()
    db.close()
    print("Libro eliminado correctamente.")

# Probar las funciones
if __name__ == "__main__":
    create_table()
    
    # Insertar algunos libros de ejemplo
    insert_book("Cien Años de Soledad", "Gabriel García Márquez", 1967, "Realismo mágico")
    insert_book("1984", "George Orwell", 1949, "Distopía")
    
    # Mostrar libros existentes
    print("\n Lista de libros:")
    for libro in get_all_books():
        print(libro)
    
    # Actualizar el libro con id 1 (es decir "Cien Años de Soledad")
   # update_book(1, "Harry Potter y la Piedra Filosofal", "JK Rowling", 1995, "Fantasía")
    
    # Eliminar el libro con id 2 (es decir "1984")
   # delete_book(2)