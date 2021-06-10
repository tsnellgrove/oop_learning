# sqlalchemy tutorial
# Jun 9, 2021

### sqlalchemy code ###
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)
session = session()
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, Numberic, String

class Cookie(Base):
		__tablename__ = 'cookies'
		
		cookie_id = Column(integer, primary_key=True)
		cookie_name = Column(String(50), index=True)
		cookie_recipie_url = Column(String(256))
		cookie_sku = Column(String(55))
		quantity = Column(Integer())
		unit_cost = Column(Numeric(12, 2))


