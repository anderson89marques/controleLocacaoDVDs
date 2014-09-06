__author__ = 'andersonmarques'

from controller import Controller

#////////  Loop principal ///////////////
sair = False
control = Controller()
control.gerar_banco()
control.cadastro_locadora()
while not sair:
    control.menu()
    r = int(input("Digite a opcao: "))
    if r in [1, 2, 3]:
        control.switch(r)
    else:
        sair = True
print("Saindo\n bye")
