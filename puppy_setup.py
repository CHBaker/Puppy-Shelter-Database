import sys

# import alchemy orm database 
# classes for mapper
from sqlalchemy import( 
	Column, ForeignKey, Integer, String, Date, Numeric)

# declarative base for 
# configuration and class code
from sqlalchemy.ext.declarative import(
	declarative_base)

# used for foreing key relationships
from sqlalchemy.orm import relationship

# used in configuration at end of file
from sqlalchemy import create_engine

# instance of base class tells alchemy
# classes correspond to tables in db
Base = declarative_base()


class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(
    	Integer, primary_key = True
    	)
    name = Column(
    	String(80), nullable = False
    	)
    address = Column(
    	String(250)
    	)
    city = Column(
    	String(80)
    	)
    state = Column(
    	String(20)
    	)
    zipCode = Column(
    	String(10)
    	)
    website = Column(
    	String
    	)

class Puppy(Base):
    __tablename__ = 'puppy'

    id = Column(
    	Integer, primary_key = True
    	)
    name = Column(
    	String(250), nullable = False
    	)
    gender = Column(
    	String(6), nullable = False
    	)
    dateOfBirth = Column(
    	Date
    	)
    picture = Column(
    	String
    	)
    shelter_id = Column(
    	Integer, ForeignKey('shelter.id')
    	)
    shelter = relationship(
    	Shelter
    	)
    weight = Column(
    	Numeric(10)
    	)


####### end of file #######

# allows us of db similar to more robust
# db like mySQL or postgreSQL
engine = create_engine('sqlite:///puppyshelter.db')

# adds tables to our db
Base.metadata.create_all(engine)