# program: dark castle v3.10
# name: Tom Snellgrove
# date: June 16, 2021
# description: db initialization module

import sqlalchemy

print(sqlalchemy.__version__)

from sqlalchemy import create_engine, Integer, Column, Sequence, JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

EntityBase = declarative_base()


class Item(EntityBase):
    __tablename__ = "items"
    id = Column(Integer, Sequence("item_id_seq"), primary_key=True, nullable=False)
    information = Column(JSON, nullable=True)


# Setup a database connection. Using in-memory database here.
engine = create_engine("sqlite://", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# Create all tables derived from the EntityBase object
EntityBase.metadata.create_all(engine)

# Declare a new row
first_item = Item()
##first_item.information = dict(a=1, b="foo", c=[1, 1, 2, 3, 5, 8, 13])
