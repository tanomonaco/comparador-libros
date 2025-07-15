from flask import Flask, jsonify, render_template, redirect, request

app = Flask(__name__)
@app.before_request
def redirect_to_custom_domain():
    # Revisa si el host de la petición es el de onrender.com
    if request.host == 'comparelibros-usa.onrender.com':
        # Si es así, crea la nueva URL con el dominio personalizado
        new_url = 'https://www.comparelibros.com' + request.full_path
        # Y le dice al navegador que se mueva permanentemente a la nueva URL
        return redirect(new_url, code=301)

# Mantenemos nuestra ruta original para saber que el sitio principal sigue vivo
@app.route("/")
def hola_mundo():
    return render_template('index.html')

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
@app.route("/privacy-policy")
def privacy_policy():
    return render_template("legal/privacy.html")

@app.route("/terms-of-service")
def terms_of_service():
    return render_template("legal/terms.html")

@app.route("/affiliate-disclosure")
def affiliate_disclosure():
    return render_template("legal/disclosure.html")
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.route("/about")
def about():
    return render_template("legal/about.html")

@app.route("/contact")
def contact():
    return render_template("legal/contact.html")
@app.route("/blog/5-classic-books")
def post1():
    return render_template("blog/post1.html")

@app.route("/blog/how-to-save-money-on-books")
def post2():
    return render_template("blog/post2.html")

@app.route("/blog/best-fantasy-series-for-new-readers")
def post3():
    return render_template("blog/post3.html")
@app.route("/blog")
def blog_index():
    return render_template("blog_index.html")