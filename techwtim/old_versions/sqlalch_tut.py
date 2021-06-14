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
from sqlalchemy import Column, Integer, Numeric, String

class Cookie(Base):
		__tablename__ = 'cookies'
		
		cookie_id = Column(Integer, primary_key=True)
		cookie_name = Column(String(50), index=True)
		cookie_recipie_url = Column(String(256))
		cookie_sku = Column(String(55))
		quantity = Column(Integer())
		unit_cost = Column(Numeric(12, 2))

Base.metadata.create_all(engine)


# insert
cc_cookie = Cookie(cookie_name='chocolate chip', cookie_recipie_url='http://some.aweso.me/cookie/choc_chip.html',
cookie_sku='CC01', quantity=12, unit_cost=0.50)

# adding to session
session.add(cc_cookie)
session.commit()

# accessing attributes
print(cc_cookie.cookie_id)

# bulk inserts
# powerful and 'light' but less 'complete'
c1 = Cookie(cookie_name='peanut butter', cookie_recipie_url='http://some.aweso.me/cookie/peanut.html',
cookie_sku='PB01', quantity=24, unit_cost=0.25)

c2 = Cookie(cookie_name='oatmeal raisin', cookie_recipie_url='http://some.okay.me/cookie/raisin.html',
cookie_sku='EWW01', quantity=100, unit_cost=1.00)

# session.bulk_save_objects([c1,c2]) # couldn't get working
session.add(c1)
session.commit()
session.add(c2)
session.commit()
# queries

# all the cookies!
cookies = session.query(Cookie).all()
print(cookies)

# all the cookies! - iterator
for cookie in session.query(Cookie):
		print(cookie)

# particular attributes
print(session.query(Cookie.cookie_name, Cookie.quantity).first())

# order by
for cookie in session.query(Cookie).order_by(Cookie.quantity):
		print('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))

# decending
from sqlalchemy import desc
for cookie in session.query(Cookie).order_by(desc(Cookie.quantity)):
		print('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))

# limiting
query = session.query(Cookie).order_by(Cookie.quantity).limit(2)
print([result.cookie_name for result in query])

# database functions
from sqlalchemy import func
inv_count = session.query(func.sum(Cookie.quantity)).scalar()
print(inv_count)

# database functions count
rec_count = session.query(func.count(Cookie.cookie_name)).first()
print(rec_count)

# labeling
rec_count = session.query(func.count(Cookie.cookie_name).label('inventory_count')).first()
print(rec_count.keys())
print(rec_count.inventory_count)

# filter_by (implicit - don't use')
record = session.query(Cookie).filter_by(cookie_name='chocolate chip').first()
print(record)

# filter (explicit - use this)
record = session.query(Cookie).filter(Cookie.cookie_name == 'chocolate chip').first()
print(record)

# clauseelements
query = session.query(Cookie).filter(Cookie.cookie_name.like('%chocolate%'))
for record in query:
		print(record.cookie_name)

# lots of cluaseelements - useful cases include in_([list]) , contains('string') , like('string')

# operators
from sqlalchemy import cast
query = session.query(Cookie.cookie_name, cast((Cookie.quantity * Cookie.unit_cost), Numeric(12,2)).label('inv_cost'))
for result in query:
		print('{} - {}'.format(result.cookie_name, result.inv_cost))

# simple query of my own
record = session.query(Cookie).filter(Cookie.cookie_name == 'peanut butter').first()
print(record.cookie_sku)

from sqlalchemy import and_, or_, not_
query = session.query(Cookie).filter(
		or_(
				Cookie.quantity.between(15, 50), Cookie.cookie_name.contains('chip')
		)
)
for result in query:
		print(result.cookie_name)

# updating cookies
query = session.query(Cookie)
cc_cookie = query.filter(Cookie.cookie_name == "chocolate chip").first()

cc_cookie.quantity = cc_cookie.quantity + 120

session.commit()
print(cc_cookie.quantity)


# deleting cookies
query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == "peanut butter")

dcc_cookie = query.one()
session.delete(dcc_cookie)
session.commit()

dcc_cookie = query.first()
print(dcc_cookie)


