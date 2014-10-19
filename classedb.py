__author__ = 'anderson'


__author__ = 'andersonmarques'
'''
    Usando o sqlalchemy para ORM e criação do banco de dados.
'''

from sqlalchemy import Column, ForeignKey, Integer, String, func
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Locadora(Base):
    __tablename__ = 'locadora'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, )
    endereco = Column()


class Departamento(Base):
    __tablename__ = 'departamento'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

class Empregado(Base):
    __tablename__ = 'empregado'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    departamento_id = Column(Integer, ForeignKey('departamento.id'))
    departamento = relationship(Departamento, backref=backref('empregados', uselist=True))

engine = None
session = None

def connectar():
    global engine #só específicando que vou usar a vriável global
    engine = create_engine('postgresql+psycopg2://postgres:nosredna89@localhost/testedb')

def criarsessao():
    global session, engine, Base

    DBSession = sessionmaker()
    DBSession.configure(bind=engine)
    session = DBSession()
    return session

def criarTabelas():
    Base.metadata.create_all(engine)

def fecharsessao(s):
    s.close()

def executar_operacoes():
    connectar()
    criarsessao()
    criarTabelas()
    session.close()
