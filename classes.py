__author__ = 'anderson'
from arquivos import *
import sys

class Cliente:
    def __init__(self, nome, telefone, endereco, codigo = 0):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.codigo = codigo

    def save(self, arquivo, f):
        arquivo.append_cliente(f, self)

    def add_codigo(self, codigo):
        self.codigo = codigo

    def __repr__(self):
        return self.nome + " " + self.endereco

class Locadora:
    def __init__(self, nome, telefone, dvds = [], clientes = [], locacoes = []):
        self.nome = nome
        self.telefone = telefone
        self.clientes = clientes
        self.dvds = dvds
        self.locacoes = locacoes

    def addDVDs(self, dvds):
        self.dvds = dvds

    def addClientes(self, clientes):
        self.clientes = clientes

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def cadastrar_dvd(self,dvd):
        self.dvds.append(dvd)

    def locar_dvds(self, cliente, dvds, locadora, preco, data_locacao, data_devolucao):
        return

    def buscar_cliente_codigo(self, codigo):
        arquivo = Arquivo()
        f = arquivo.open_arquivo("clientedb.txt", "r+")
        dados = arquivo.buscar_cliente_codigo(f, codigo)
        cliente = Cliente(dados[1], dados[2], dados[3], int(dados[0]))
        arquivo.fecha_arquivo(f)
        return cliente

    #como se fosse código de barra
    def buscar_dvds_codigo(self, codigo):
        arquivo = Arquivo()
        f = arquivo.open_arquivo("dvddb.txt", "r+")
        dados = arquivo.buscar_dvd_por_codigo(f,codigo)
        dvd = DVD(dados[0], dados[1], int(dados[2]))
        print(dvd)
        arquivo.fecha_arquivo(f)
        return dvd

    def save_clientes(self):
        arquivo = Arquivo()
        f = arquivo.open_arquivo("clientedb.txt","a")
        l = arquivo.adicionar_codigo("clientedb.txt")

        for cliente in self.clientes:
            l += 1
            cliente.add_codigo(l)
            cliente.save(arquivo, f)

        arquivo.fecha_arquivo(f)

    def save_dvds(self):
        arquivo = Arquivo()
        f = arquivo.open_arquivo("dvddb.txt","a")
        l = arquivo.adicionar_codigo("dvddb.txt")

        for dvd in self.dvds:
            l += 1
            dvd.add_codigo(l)
            dvd.save(arquivo, f)

        arquivo.fecha_arquivo(f)

    def __repr__(self):
        return self.nome + " " + self.telefone

class Locacao:
    preco_locacao_por_dvd = 3 #R$ 3,00
    def __init__(self, cliente, dvds):
        self.codigo = self.buscar_codigo()
        self.cliente = cliente
        self.dvds = dvds
        self.data_locacao = None
        self.data_devolucao = None
        self.status = None

    def locacao(self):
        arquivo = Arquivo()
        f = arquivo.open_arquivo("locacaodb.txt", "w")
        arquivo.locacao(f,self.codigo, self.cliente, self.dvds)
        arquivo.fecha_arquivo(f)
        return

    def buscar_codigo(self):
        arquivo = Arquivo()
        codigo = arquivo.adicionar_codigo("locacaodb.txt")
        return codigo

    def __repr__(self):
        return self.cliente + " " + self.preco

class DVD:
    def __init__(self, nome, genero, codigo = 0):
        self.codigo = codigo
        self.nome = nome
        self.genero = genero

    def save(self, arquivo, f):
        arquivo.append_dvd(f, self)
        return

    def add_codigo(self, codigo):
        self.codigo = codigo

    def __repr__(self):
        return self.nome + " " + self.genero