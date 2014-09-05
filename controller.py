__author__ = 'andersonmarques'
from banco.classesdb import *

class Controller():
    def __init__(self):
        self.dic = {1: self.cadastro_cliente, 2: self.fazer_locacao, 3: self.cadastro_dvds}
        self.sair = False
        self.cliente = None
        self.locadora = None

    def gerar_banco(self):
        executar_operacoes()

    def cadastro_locadora(self):
        connectar()
        sessao = criarsessao()
        self.locadora = Locadora(nome="Minha Locadora", telefone="(91)98765432")
        sessao.add(self.locadora)
        sessao.commit()
        fecharsessao(sessao)

    def cadastro_cliente(self):
        pass

    def cadastro_dvds(self):
        pass

    def fazer_locacao(self):
        pass

    def switch(self, w):
        self.dic[w]()

    def menu(self):
        msg = '''
        1 - cadastrar cliente
        2 - fazer locacao
        3 - cadastrar DVDs
        0 - sair
        '''
        print(msg)



