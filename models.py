from sqlalchemy import Column, String, Integer, Text

from database import Base

class Dish(Base):
    __tablename__ = 'Dish'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    cooking_time = Column(Integer, index=True)
    ingredients = Column(String, index=True)
    recipe = Column(Text, index=True)
    views = Column(Integer, index=True, default=0)
