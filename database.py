from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Flavor, Ingredient, Allergen, CustomerSuggestion, CartItem

class Database:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # Create tables if they do not exist
        Base.metadata.create_all(self.engine)

    def add_flavor(self, name, description, price):
        flavor = Flavor(name=name, description=description, price=price)
        self.session.add(flavor)
        self.session.commit()

    def add_ingredient(self, name, quantity, unit):
        ingredient = Ingredient(name=name, quantity=quantity, unit=unit)
        self.session.add(ingredient)
        self.session.commit()

    def add_allergen(self, name):
        allergen = Allergen(name=name)
        self.session.add(allergen)
        self.session.commit()

    def add_customer_suggestion(self, suggestion, email):
        suggestion = CustomerSuggestion(suggestion=suggestion, email=email)
        self.session.add(suggestion)
        self.session.commit()

    def add_to_cart(self, flavor_id, quantity):
        cart_item = CartItem(flavor_id=flavor_id, quantity=quantity)
        self.session.add(cart_item)
        self.session.commit()

    def get_cart_items(self):
        return self.session.query(CartItem).all()

    def close(self):
        self.session.close()
