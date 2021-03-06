__author__ = 'anderson'
from banco_arquivos.classes import *
from arquivos import *

sair = False
cliente = None

def criar_arquivos_db():
    arquivo = Arquivo()

    arquivo.cria_arquivo_locadora()
    arquivo.cria_arquivo_cliente()
    arquivo.cria_arquivo_dvd()
    arquivo.cria_arquivo_locacao()
    arquivo.cria_locacao_dvd()

def cadastro_locadora():
    f = open("locadoradb.txt","r")
    a,b = f.readline().split(" ")
    print(a)
    print(b)
    f.close()
    locadora = Locadora(a,b)
    return locadora

#locadora = cadastro_locadora()

def cadastro_cliente():
    global locadora
    dici = [ "Nome", "Telefone", "Endereco"]
    sair = False

    print("\n\n******** %s ********\n" %"Cadastrado de Clientes")
    while not sair:
        r = processa(dici)
        sair = r[1]
        if(len(r[0]) == 3):
            cliente = Cliente(r[0][0], r[0][1], r[0][2])
            locadora.addClientes([cliente])
            print(locadora.clientes)
            locadora.save_clientes()

            x = input("continuar cadastro? (S/N)")
            if x.lower() == 'n':
                sair = True

def fazer_locacao():
    global locadora
    codigo = input("Digite o código do cliente:")
    cliente = locadora.buscar_cliente_codigo(codigo)
    dvds = buscar_dvds(locadora)
    print(cliente)
    print(dvds)
    locacao = Locacao(cliente, dvds)
    locacao.locacao()

def buscar_dvds(locadora):
    sair = False
    dvds = []
    while not sair:
        codigo = input("Digite o código do dvd:")
        dvds.append(locadora.buscar_dvds_codigo(codigo))
        msg = input("continuar?(s/n):").lower()
        if msg == "n":
            sair = True
    return dvds

def cadastrar_dvds():
    global locadora
    dici = [ "Nome", "Genero"]
    sair = False
    r = []
    print("\n\n******** %s ********\n" %"Cadastrado de DVDs")
    while not sair:
        r = processa(dici)
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

def switch(w):
    dic[w]()

def menu():
    msg = '''
    1 - cadastrar cliente
    2 - fazer locacao
    3 - cadastrar DVDs
    0 - sair
    '''
    print(msg)

dic = {1 : cadastro_cliente, 2 : fazer_locacao, 3 : cadastrar_dvds}

#criar_arquivos_db()
#cadastro_locadora()

#////////  Loop principal ///////////////
while not sair:
    menu()
    r = int(input("Digite a opcao: "))
    if r in [1, 2, 3]:
        switch(r)
    else:
        sair = True

print("Saindo\n bye")