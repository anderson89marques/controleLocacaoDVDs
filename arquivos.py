__author__ = 'anderson'

class Arquivo:
    def open_arquivo(self,nome,modo):
        f = open(nome,modo)
        return f

    def fecha_arquivo(self, f):
        f.close

    def cria_arquivo_locadora(self):
        f = open("locadoradb.txt","w")
        f.write("%s %s" %("LocaDVDS","(91)84328608"))
        f.close()

    def cria_arquivo_cliente(self):
        f = open("clientedb.txt","w")
        f.close()

    def cria_arquivo_locacao(self):
        f = open("locacaodb.txt","w")
        f.close()

    def cria_aquivo_dvd(self):
        f = open("dvddb.txt","w")
        f.close()

    def adicionar_codigo(self, nome):
        l = len(open(nome, "r").readlines())
        return l

    def append_cliente(self,f, cliente):
        f.write("%s %s %s %s\n" %(cliente.codigo, cliente.nome, cliente.telefone, cliente.endereco))

    def append_dvd(self, f, dvd):
        f.write("%s %s %s\n" %(dvd.codigo, dvd.nome, dvd.genero))

    def buscar_cliente_codigo(self,codigo):
        pass