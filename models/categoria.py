#importar modelo base 
from  db import Base
#importaciones de las clase sqllalchemy
from sqlalchemy import Column, Integer, String

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, 
                primary_key=True)
    nombre = Column(String(100))