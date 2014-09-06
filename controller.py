__author__ = 'andersonmarques'
from banco.classesdb import *

class Controller():
    def __init__(self):
        self.dic = {1: self.cadastro_cliente, 2: self.fazer_locacao, 3: self.cadastro_dvds}
        self.sair = False
        self.cliente = None
        self.managerdb = Managerdb()
        self.locadora = self.buscar_locadora()
        self.managerdb.connectar()

    def gerar_banco(self):
        self.managerdb.executar_operacoes()
        if self.locadora == None:
            self.locadora = self.buscar_locadora()

    def cadastro_locadora(self):
        self.managerdb.criarsessao()
        sessao = self.managerdb.session
        try:
            l = sessao.query(Locadora).one()
            self.locadora = l
            print("loc1")
        except Exception:
            print("loc2")
            self.locadora = Locadora(nome="Minha Locadora", telefone="(91)98765432")
            sessao.add(self.locadora)
            sessao.commit()
        self.managerdb.fecharsessao()

    def buscar_locadora(self):
        self.managerdb.criarsessao()
        s = self.managerdb.session
        try:
            l = s.query(Locadora).first()
        except Exception:
            l = None
        print("Locadora rapaz:{0}".format(l)) if l else print("Aqui rapaz")
        s.close()
        return l

    def cadastro_cliente(self):
        dici = [ "Nome", "Telefone", "Endereco"]
        sair = False
        self.managerdb.criarsessao()
        s = self.managerdb.session
        print("\n\n******** %s ********\n" %"Cadastrado de Clientes")
        while not sair:
            r = self.processa(dici)
            sair = r[1]
            if(len(r[0]) == 3):
                cliente = Cliente(nome=r[0][0], telefone=r[0][1], endereco=r[0][2])
                print("{0}".format(cliente))
                cliente.locadora = self.locadora
                s.add(cliente)
                print(self.locadora.clientes)
                x = input("continuar cadastro? (S/N)")
                if x.lower() == 'n':
                    sair = True
                    s.add(self.locadora)
                    s.commit()
        s.close()

    def cadastro_dvds(self):
        dici = [ "Nome", "Genero"]
        sair = False
        r = []
        self.managerdb.criarsessao()
        s = self.managerdb.session
        print("\n\n******** %s ********\n" %"Cadastrado de DVDs")
        while not sair:
            r = self.processa(dici)
            sair = r[1]
            if len(r[0]) == 2:
                dvd = Dvd(nome=r[0][0], genero=r[0][1])
                dvd.locadora = self.locadora
                s.add(dvd)
                print(self.locadora.dvds)

                x = input("\ncontinuar cadastro? (S/N)")
                if x.lower() == 'n':
                    sair = True
                    s.add(self.locadora)
                    s.commit()
        s.close()

    def processa(self, dici):
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



