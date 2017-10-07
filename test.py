'''
Goal:
User, Org, List objects
User and list belong to Org
Given UID and OrgID, return all List objects the user can access in that Org.

http://docs.sqlalchemy.org/en/latest/orm/join_conditions.html
http://docs.sqlalchemy.org/en/latest/orm/backref.html

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

ed_user = User(name='ed', fullname='Ed Jones', password='hunter2')
session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()
print(our_user)
