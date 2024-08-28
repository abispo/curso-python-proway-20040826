"""
Funções (Procedures)

Parâmetros arbitrários

No Python, podemos criar funções que recebem uma quantidade qualquer de parâmetros. É um recurso utilizado principalmente quando criamos decorators
"""

def calcula_media_valores(*args):
    try:
        return sum(args) / len(args)
    except ZeroDivisionError:
        return 0
    

def mostra_info_usuario(**kwargs):
    print('*'*50)
    print("* INFO USUÁRIO ***")
    for chave, valor in kwargs.items():
        print(f"* {chave}: {valor}")
    print('*'*50)

if __name__ == "__main__":
    
    print("Zero parâmetros: {}".format(calcula_media_valores()))
    print("Um parâmetro: {}".format(calcula_media_valores(2)))
    print("Vários parâmetros: {}".format(
        calcula_media_valores(1, 5, 8, 4, 5, 2))
    )
    lista_valores = (10, 60, 43, 62, 11, 19,)
    print("Vários parâmetros: {}".format(
        calcula_media_valores(*lista_valores))
    )

    mostra_info_usuario(
        nome="Maria", idade=25, genero='F', cidade="Blumenau"
    )

    usuario1 = {
        "nome": "João",
        "idade": 80
    }

    mostra_info_usuario(**usuario1)
