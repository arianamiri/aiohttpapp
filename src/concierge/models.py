from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from concierge.utils.db import Base, connection


class Stylist(Base):
    """
    Orm class for stylists
    """
    __tablename__ = 'stylist'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    assortments = relationship('Assortment', back_populates='stylist')


class Customer(Base):
    """
    Orm class for customers
    """
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    assortments = relationship('Assortment', back_populates='customer')


class Assortment(Base):
    """
    Orm class for assortments.

    An assortment is a collection of "picks" (aka products) that a stylist
    has chosen for a customer.
    """
    __tablename__ = 'assortment'

    id = Column(Integer, primary_key=True)
    stylist_id = Column(Integer, ForeignKey('stylist.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))

    stylist = relationship('Stylist', back_populates='assortments')
    customer = relationship('Customer', back_populates='assortments')
    picks = relationship('Picks', back_populates='assortment')


class Picks(Base):
    """
    Orm class for picks.abs

    This is a product that has been recommmended to a user as part of an
    assortment.
    """
    __tablename__ = 'picks'

    id = Column(Integer, primary_key=True)
    ruecom_id = Column(Integer)

    assortment_id = Column(Integer, ForeignKey('assortment.id'))

    assortment = relationship('Assortment', back_populates='picks')
