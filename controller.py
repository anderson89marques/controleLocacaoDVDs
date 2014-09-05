from main import buscar_dvds

__author__ = 'andersonmarques'
from banco.classesdb import *

class Controller():
    def __init__(self):
        self.dic = {1: self.cadastro_cliente, 2: self.fazer_locacao, 3: self.cadastro_dvds}
        self.sair = False
        self.cliente = None
        self.locadora = self.buscar_locadora()

    def gerar_banco(self):
        executar_operacoes()

    def cadastro_locadora(self):
        connectar()
        sessao = criarsessao()
        self.locadora = Locadora(nome="Minha Locadora", telefone="(91)98765432")
        sessao.add(self.locadora)
        sessao.commit()
        fecharsessao(sessao)

    def buscar_locadora(self):
        connectar()
        s = criarsessao()
        return s.query(Locadora).one()

    def cadastro_cliente(self):
        dici = [ "Nome", "Telefone", "Endereco"]
        sair = False
        connectar()
        s = criarsessao()
        print("\n\n******** %s ********\n" %"Cadastrado de Clientes")
        while not sair:
            r = self.processa(dici)
            sair = r[1]
            if(len(r[0]) == 3):
                cliente = Cliente(r[0][0], r[0][1], r[0][2])
                s.add(cliente)
                self.locadora.clientes(cliente)

                print(locadora.clientes)
                locadora.save_clientes()

                x = input("continuar cadastro? (S/N)")
                if x.lower() == 'n':
                    sair = True

    def cadastro_dvds(self):
        dici = [ "Nome", "Genero"]
        sair = False
        r = []
        print("\n\n******** %s ********\n" %"Cadastrado de DVDs")
        while not sair:
            r = self.processa(dici)
            sair = r[1]
            if len(r[0]) == 2:
                dvd = DVD(r[0][0], r[0][1])
                locadora.addDVDs([dvd])
                print(locadora.dvds)
                locadora.save_dvds()

                x = input("\ncontinuar cadastro? (S/N)")
                if x.lower() == 'n':
                    sair = True

    def processa(dici):
        sair = False
        r = []
        resp = []
        for d in dici:
            x = input("Digite o %s: (zero para sair)" %d)
            if(x == "0"):
                sair = True
                break
            resp.append(x)
        r.append(resp)
        r.append(sair)
        return r

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



