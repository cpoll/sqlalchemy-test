'''
http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
'''

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)


Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

# Add Ed
ed_user = User(name='ed', fullname='Ed Jones', password='hunter2')
session.add(ed_user)

# Get Ed
queried_ed_user = session.query(User).filter_by(name='ed').first()
print(queried_ed_user)

# Add multi
session.add_all([
    User(name='wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxg527'),
    User(name='fred', fullname='Fred Flinstone', password='blah')])

# Change Ed's password
queried_ed_user.password = 'hunter3'

# Look at pending operations
print(session.dirty)
print(session.new)
session.commit()