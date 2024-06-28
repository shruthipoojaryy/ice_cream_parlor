from database import Database
from models import Flavor, Ingredient, Allergen, CustomerSuggestion, CartItem
from database import db

def search_flavors(search_term):
    results = db.session.query(Flavor).filter(Flavor.name.ilike(f'%{search_term}%')).all()
    return results


def add_flavor(name, description, price):
    db = Database('ice_cream_parlor.db')
    db.cursor.execute("INSERT INTO flavors (name, description, price) VALUES (?, ?, ?)", (name, description, price))
    db.conn.commit()
    db.close()

def add_ingredient(name, quantity, unit):
    db = Database('ice_cream_parlor.db')
    db.cursor.execute("INSERT INTO ingredients (name, quantity, unit) VALUES (?, ?, ?)", (name, quantity, unit))
    db.conn.commit()
    db.close()

def add_allergen(name):
    db = Database('ice_cream_parlor.db')
    db.cursor.execute("INSERT INTO allergens (name) VALUES (?)", (name,))
    db.conn.commit()
    db.close()

def add_suggestion(suggestion, email):
    db = Database('ice_cream_parlor.db')
    db.cursor.execute("INSERT INTO customer_suggestions (suggestion, email) VALUES (?, ?)", (suggestion, email))
    db.conn.commit()
    db.close()

def add_to_cart(flavor_id, quantity):
    db = Database('ice_cream_parlor.db')
    db.cursor.execute("INSERT INTO customer_cart (flavor_id, quantity) VALUES (?, ?)", (flavor_id, quantity))
    db.conn.commit()
    db.close()

def search_flavors(name):
    db = Database('ice_cream_parlor.db')
    db.cursor.execute("SELECT * FROM flavors WHERE name LIKE ?", ('%' + name + '%',))
    results = db.cursor.fetchall()
    db.close()
    return [Flavor(*row) for row in results]

def filter_flavors(min_price, max_price):
    db = Database('ice_cream_parlor.db')
    db.cursor.execute("SELECT * FROM flavors WHERE price BETWEEN ? AND ?", (min_price, max_price))
    results = db.cursor.fetchall()
    db.close()
    return [Flavor(*row) for row in results]

def get_cart_items():
    db = Database('ice_cream_parlor.db')
    db.cursor.execute("SELECT c.id, c.flavor_id, c.quantity, f.name, f.description, f.price "
                     "FROM customer_cart c "
                     "JOIN flavors f ON c.flavor_id = f.id")
    results = db.cursor.fetchall()
    db.close()
    cart_items = []
    for row in results:
        cart_item = CartItem(*row[:3])
        cart_item.flavor = Flavor(*row[3:])
        cart_items.append(cart_item)
    return cart_items