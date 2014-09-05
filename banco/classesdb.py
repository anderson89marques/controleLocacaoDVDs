__author__ = 'andersonmarques'

'''
    Exemplo de um relacionamento 1-to-n usando o sqlalchemy
'''

from sqlalchemy import Column, ForeignKey, Integer, String, Date, func
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Locadora(Base):
    __tablename__ = 'locadora'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    codigo = Column(Integer, nullable=True)
    locadora_id = Column(Integer, ForeignKey('locadora.id'))
    locadora = relationship(Locadora, backref=backref('clientes', uselist=True))

    def __repr__(self):
        return "[cliente: nome:{0} endereço:{1}]".format(self.nome, self.endereco)

class Locacao(Base):
    __tablename__ = 'locacao'
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=False)
    data_locacao = Column(String, nullable=False)
    data_devolucao = Column(String, nullable=False)
    status = Column(String, nullable=False)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship(Cliente, backref=backref('locacoes', uselist=True))

    def __repr__(self):
       return "[locação: status:{0} {1}]".format(self.status, self.cliente)

class Dvd(Base):
    __tablename__ = 'dvd'
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=False)
    nome = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    locadora_id = Column(Integer, ForeignKey('locadora.id'))
    locadora = relationship(Locadora, backref=backref('dvds', uselist=True))
    locacao_id = Column(Integer, ForeignKey('locacao.id'))
    locacao = relationship(Locacao, backref=backref('dvds', uselist=True))

    def __repr__(self):
        return "[DVD: nome:{0} genero:{1}]".format(self.nome, self.genero)

engine = None
session = None

def connectar():
    global engine #só específicando que vou usar a vriável global
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/pythonestudo')

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
    s = criarsessao()
    criarTabelas()
    fecharsessao(s)
