#imagina um sistem q recolha escolha o usario
# escolha usuario
#  se
# 0 ---> sair do progama
# 1 ---> entrar no progama
# -----> Erro!
while True:
    print("Hello, world!")
    print(""" 0 = Continuar
1 = Parar""")

    escolha_usuario = int(input("vc quer continuar? "))

    match escolha_usuario:
        case 0:
            continue  # volta pro início do loop
        case 1:
            print("FIM!")
            break  # sai do loop
        case _:
            print("Erro!")