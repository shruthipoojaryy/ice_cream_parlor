from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Flavor(Base):
    __tablename__ = 'flavors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    unit = Column(String)

class Allergen(Base):
    __tablename__ = 'allergens'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class CustomerSuggestion(Base):
    __tablename__ = 'customer_suggestions'
    id = Column(Integer, primary_key=True)
    suggestion = Column(String)
    email = Column(String)

class CartItem(Base):
    __tablename__ = 'customer_cart'
    id = Column(Integer, primary_key=True)
    flavor_id = Column(Integer, ForeignKey('flavors.id'))
    quantity = Column(Integer)
