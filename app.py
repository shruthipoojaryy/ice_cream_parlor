from flask import Flask, render_template, request, redirect, url_for
from database import Database
from models import Flavor, Ingredient, Allergen, CustomerSuggestion

app = Flask(__name__)
db = Database('sqlite:///ice_cream_parlor.db')  # Replace with your actual database URI

@app.route('/')
def index():
    flavors = db.session.query(Flavor).all()
    return render_template('index.html', flavors=flavors)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        flavors = db.session.query(Flavor).filter(Flavor.name.ilike(f'%{search_term}%')).all()
        return render_template('index.html', flavors=flavors)
    return render_template('search.html')

@app.route('/filter', methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        min_price = float(request.form['min_price'])
        max_price = float(request.form['max_price'])
        flavors = db.session.query(Flavor).filter(Flavor.price >= min_price, Flavor.price <= max_price).all()
        return render_template('index.html', flavors=flavors)
    return render_template('filter.html')

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        flavor_id = int(request.form['flavor_id'])
        quantity = int(request.form['quantity'])
        db.add_to_cart(flavor_id, quantity)
        return redirect(url_for('cart'))
    cart_items = db.get_cart_items()
    return render_template('cart.html', cart_items=cart_items)

@app.route('/ingredients')
def ingredients():
    ingredients = db.session.query(Ingredient).all()
    return render_template('ingredients.html', ingredients=ingredients)

@app.route('/allergens')
def allergens():
    allergens = db.session.query(Allergen).all()
    return render_template('allergens.html', allergens=allergens)

@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    if request.method == 'POST':
        suggestion = request.form['suggestion']
        email = request.form['email']
        db.add_customer_suggestion(suggestion, email)
        return redirect(url_for('suggestions'))
    
    suggestions = db.session.query(CustomerSuggestion).all()
    return render_template('suggestions.html', suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
