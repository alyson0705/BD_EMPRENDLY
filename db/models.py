
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Usuarios(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(40))
    correo = Column(String(100))
    contraseña = Column(String(40))
    rol = Column(String(60))


class Productos(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(40))
    categoria = Column(String(60))
    precio_unitario = Column(String(60))
    fecha_registro = Column(String(60))
  

class MediosPago(Base):
    __tablename__= "mediospago"
    id= Column(Integer , primary_key=True)
    nombre= Column (String(100))


class Ventas(Base):
    __tablename__= "ventas"
    id = Column (Integer , primary_key=True)
    producto_id= Column(Integer, ForeignKey("productos.id"))
    medio_pago_id= Column(Integer, ForeignKey("mediospago.id"))
    valor= Column (String(100))
    cantidad= Column (String(100))
    fecha_registro = Column(String(60))

class Gastos(Base):
    __tablename__= "gastos"
    id= Column(Integer , primary_key=True)
    valor= Column (String(100))
    tipo= Column (String(100))
    fecha= Column (String(100))