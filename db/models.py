from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


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
    descripcion = Column(String(60))
    categoria = Column(String(60))
    unidad_medida = Column(String(60))
    precio_unitario = Column(String(60))  # Usa Float si es número
    fecha_registro = Column(String(60))


class Costoslog(Base):
    __tablename__ = "costoslog"
    id = Column(Integer, primary_key=True)
    categoria = Column(String(100))
    descripcion = Column(String(100))


class Inventario_movimientos(Base):
    __tablename__ = "inventario_movimientos"
    id_movimiento = Column(Integer, primary_key=True)
    id_producto = Column(String(50))
    cantidad = Column(String(50))
    fecha_movimiento = Column(String(50))
    observaciones = Column(String(50))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))


class Costospr(Base):
    __tablename__ = "costospr"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    valor = Column(String(100))
    monto = Column(String(100))


class Ordenes(Base):
    __tablename__ = "ordenes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    valor = Column(String(100))
    fecha = Column(String(100))
    numero_orden = Column(String(100))


class Detalles(Base):
    __tablename__ = "detalles"
    id = Column(Integer, primary_key=True)
    detalle = Column(String(100))
    valor = Column(String(100))
    producto = Column(String(100))
    cantidad = Column(String(100))
