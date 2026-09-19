from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    stage = input("Etapa no funil ")

    control.create_lead(model_lead (name, email, stage))


    print(model_lead(name,email,stage))

    print("Leads adicionados (func)")


def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
            print("lead adicionado")
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção invalida...")

if __name__ == "__main__":
    main()