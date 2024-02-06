import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column (String, nullable = False)
    subscription_date= Column (DateTime, nullable = False)
    favorite = relationship ('favorite')
                               

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    planet_description = Column(String(250))
    image_url = Column (String (150), nullable = True)
    favorite = relationship ('favorite')

class Favorite(Base):
     __tablename__ = 'favorite'
     id = Column(Integer, primary_key=True)
     planet_id = Column (Integer, ForeignKey('planet.id'), nullable= True)
     character_id = Column (Integer, ForeignKey('character.id'), nullable= True)
     user_id = Column (Integer, ForeignKey('user.id'), nullable= False)
     vehicle_id = Column (Integer, ForeignKey('vehicle.id'), nullable= True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    caracther_name = Column(String(250))
    caracther_description = Column(String(250))
    image_url = Column (String (150), nullable = True)
    favorite= relationship ('favorite')


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250))
    vehicle_description = Column(String(250))
    image_url = Column (String (150), nullable = True)
    favorite= relationship ('favorite')



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
