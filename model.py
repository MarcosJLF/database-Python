from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv('URL_DB')

DATABASE_URI = database_url
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

class Pais(Base):
    __tablename__ = 'pais'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    sigla = Column(String)
    populacao = Column(Integer)
    data_atualizacao = Column(DateTime)

    estados = relationship('Estado', back_populates='pais')

class Estado(Base):
    __tablename__ = 'estado'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    sigla = Column(String)
    pais_id = Column(Integer, ForeignKey('pais.id'))

    pais = relationship('Pais', back_populates='estados')

Base.metadata.create_all(engine)
