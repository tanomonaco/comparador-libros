from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Mantenemos nuestra ruta original para saber que el sitio principal sigue vivo
@app.route("/")
def hola_mundo():
    return return render_template('index.html')

# ¡NUEVA RUTA! Esta es nuestra primera API de búsqueda
@app.route("/api/search/<string:isbn>")
def search_book(isbn):
    """
    Esta función simula la búsqueda de un libro por ISBN.
    Más adelante, aquí haremos las llamadas reales a las tiendas.
    """
    print(f"Recibida búsqueda para el ISBN: {isbn}")

    # Simulamos que encontramos un libro en nuestra base de datos
    dummy_book_data = {
        "isbn_recibido": isbn,
        "titulo": "Harry Potter and the Philosopher's Stone",
        "autor": "J.K. Rowling",
        "precios": [
            {
                "tienda": "Amazon.com",
                "precio": 19.99,
                "moneda": "USD",
                "link": f"https://amazon.com/dp/{isbn}"
            },
            {
                "tienda": "BuscaLibre",
                "precio": 18.50,
                "moneda": "USD",
                "link": f"https://buscalibre.com/libros/search?q={isbn}"
            }
        ]
    }

    # Devolvemos los datos en formato JSON, el lenguaje de las APIs
    return jsonify(dummy_book_data)