from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppy_setup import Base, Shelter, Puppy
from datetime import timedelta
import datetime

# tells which db engine to talk to
engine = create_engine('sqlite:///puppyshelter.db')

# connects classes to tables in db
Base.metadata.bind = engine

# link between code execution and engine
DBSession = sessionmaker(bind = engine)

# instance of session allows CRUD executions sql after a commit
session = DBSession()

# returns all puppies in alphabetical order

puppies = session.query(Puppy).order_by(Puppy.name)
for puppy in puppies:
	print puppy.name

# query all of the puppies that are less than 
# 6 months old organized by the youngest first

six_mos_before = datetime.date.today()-datetime.timedelta(days=180)
puppies = session.query(Puppy).filter(
	Puppy.dateOfBirth > six_mos_before).order_by(
	Puppy.dateOfBirth.desc()).all()
for pup in puppies: 
	print pup.name, pup.dateOfBirth

# query all puppies by weight asc

fatties = session.query(
	Puppy).order_by(Puppy.weight.asc()).all()
for puppy in fatties:
	print puppy.name, puppy.weight

# query puppies grouped by shelter

pups = session.query(Puppy).order_by(Puppy.shelter_id).all()
for pup in pups:
	print pup.name, pup.shelter.name



