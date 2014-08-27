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

    def save_clientes(self):
        arquivo = Arquivo()
        f = arquivo.open_arquivo("clientedb.txt")
        l = arquivo.adicionar_codigo("clientedb.txt")

        for cliente in self.clientes:
            l += 1
            cliente.add_codigo(l)
            cliente.save(arquivo, f)

        arquivo.fecha_arquivo(f)

    def save_dvds(self):
        arquivo = Arquivo()
        f = arquivo.open_arquivo("dvddb.txt")
        l = arquivo.adicionar_codigo("dvddb.txt")

        for dvd in self.dvds:
            l += 1
            dvd.add_codigo(l)
            dvd.save(arquivo, f)

        arquivo.fecha_arquivo(f)

    def __repr__(self):
        return self.nome + " " + self.telefone

class Locacao:
    def __init__(self, cliente, dvds, locadora, preco, data_locacao, data_devolucao,codigo = 0):
        self.codigo = codigo
        self.cliente = cliente
        self.dvds = dvds
        self.locadora = locadora
        self.preco = preco
        self.data_locacao = data_locacao
        self.data_devolucao = data_devolucao

    def save(self):
        return

    def add_codigo(self, codigo):
        self.codigo = codigo

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