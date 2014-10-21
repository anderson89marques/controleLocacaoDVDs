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
    senha = Column(String, nullable=False)
    clientes = relationship("Cliente", back_populates='locadora')
    dvds = relationship("Dvd", back_populates='locadora')
    preco_locacao_por_dvd = 3.0

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    codigo = Column(Integer, nullable=True)
    locadora_id = Column(Integer, ForeignKey('locadora.id'))
    locadora = relationship(Locadora, back_populates='clientes')
    locacoes = relationship("Locacao", back_populates='cliente')

    def __repr__(self):
        return "[cliente: nome:{0} endereço:{1}]".format(self.nome, self.endereco)

class Locacao(Base):
    __tablename__ = 'locacao'
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=False)
    data_locacao = Column(String, nullable=False)
    data_devolucao = Column(String, nullable=False)
    preco = Column(String, nullable=False) #mudar depois para float
    status = Column(String, nullable=False)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship(Cliente, back_populates='locacoes')
    dvds = relationship("Dvd", back_populates='locacao')

    def __repr__(self):
       return "[locação: status:{0} {1}]".format(self.status, self.cliente)

class Dvd(Base):
    __tablename__ = 'dvd'
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=True)
    nome = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    locadora_id = Column(Integer, ForeignKey('locadora.id'))
    locadora = relationship(Locadora, back_populates='dvds')
    locacao_id = Column(Integer, ForeignKey('locacao.id'))
    locacao = relationship(Locacao, back_populates='dvds')

    def __repr__(self):
        return "[DVD: nome:{0} genero:{1}]".format(self.nome, self.genero)

class Managerdb():
    def __init__(self):
        self.engine = None
        self.session = None

    def connectar(self):
        self.engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/pythonestudo')

    def criarsessao(self):
        DBSession = sessionmaker()
        DBSession.configure(bind=self.engine)
        self.session = DBSession()

    def criarTabelas(self):
        Base.metadata.create_all(self.engine)

    def fecharsessao(self):
        self.session.close()

    def executar_operacoes(self):
        self.connectar()
        self.criarsessao()
        self.criarTabelas()
        self.fecharsessao()
