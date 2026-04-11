#imagina um sistem q recolha escolha o usario
# escolha usuario
#  se
# 0 ---> sair do progama
# 1 ---> entrar no progama
# -----> Erro!

escolha_usuario = 1234

match escolha_usuario:
    case 0:
        print("Sair do progama")
    case 1:
        print("entrar no progama")
    case _:
        print("Erro!")