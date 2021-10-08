# program: dark castle v3.10
# name: Tom Snellgrove
# date: June 16, 2021
# description: db initialization module

## import sqlalchemy
## print(sqlalchemy.__version__)

## import sqlite3
### print(sqlite3.sqlite_version_info)

# Updated sqlalchemy to version 1.1.2 to gain JSON support
# Got to command line using launch_stash.py from iPad directory
# then followed manual update directions found here:
# https://forum.omz-software.com/topic/2642/updating-sqlalchemy-from-0-9-7-to-1-1
# updated from 1.0.11 => 1.1.2 as 1.0.11 still gave JSON error
# updated to 1.4.18 and installed importlib_metadata and typing_extensions
# NOW APPEARS TO RUN!!!

from sqlalchemy import create_engine, Integer, Column, Sequence, JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def db_init():
		EntityBase = declarative_base()


		class Itemdb(EntityBase):
				__tablename__ = "items"
				id = Column(Integer, Sequence("item_id_seq"), primary_key=True, nullable=False)
				information = Column(JSON, nullable=True)


# Setup a database connection. Using in-memory database here.
		engine = create_engine("sqlite://", echo=False)

		Session = sessionmaker(bind=engine)
		session = Session()

# Create all tables derived from the EntityBase object
		EntityBase.metadata.create_all(engine)

# Declare a new row
##		first_item = Itemdb()
		stateful_db = Itemdb()
##first_item.information = dict(a=1, b="foo", c=[1, 1, 2, 3, 5, 8, 13])
		return stateful_db, session
		
		
### wrapper db_init calls pre-pickle ###

# wrapper code - sets up game state and calls interpreter
def wrapper_demo(user_input, stateful_dict):

### def wrapper(user_input):
		if user_input == "xyzzy42":
				pass

####				stateful_db, session = db_init()

		else:
				pass

####				stateful_dict = stateful_db.information


		interpreter(stateful_dict, user_input)

####		stateful_db.information = stateful_dict
####		session.add(stateful_db)
####		session.commit()

		return stateful_dict['end_of_game'], stateful_dict['out_buff']
