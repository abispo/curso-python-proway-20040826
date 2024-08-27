"""
Programa que testa o nível de acesso do usuário

"""

from prog02 import lista1

if __name__ == "__main__":

    print(lista1)
    nivel_acesso = int(input("Informe o seu nível de acesso (1-4): "))

    match nivel_acesso:
        case 1:
            print("Nível de acesso: Usuário.")

        case 2:
            print("Nível de acesso: Gerente.")

        case 3:
            print("Nível de acesso: Administrador.")

        case 4:
            print("Nível de acesso: root.")

        case _:
            print("Nível de acesso desconhecido.")