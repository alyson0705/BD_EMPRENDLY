from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#variable cadena de conexion:
MARIADB_URL= 'mysql+pymysql://root:admin@localhost:3315/pyshop'

#crear el objeto de conexion la base de datos
engine= create_engine(MARIADB_URL) 

#plantilla base para los modelos 
Base = declarative_base()
