from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy import TIMESTAMP, Column,Integer, String , Boolean


class Recipe(Base):
    __tablename__ = "recipe"
    id = Column(Integer, primary_key= True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

