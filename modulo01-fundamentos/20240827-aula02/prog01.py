"""
Laços de condição

Laço for

O laço for geralmente é utilizado quando precisamos percorrer uma sequência de valores, que pode ser uma lista, um dicionário, uma string, ou qualquer outro tipo de container.

container = estrutura que contém outros tipos de dados.

Quando uma estrutura permite que os seus valores sejam acessados sequencialmente por um comando for, dizemos que essa estrutura é iterável.
"""

from random import randint

if __name__ == "__main__":

    curso = "Python"

    for letra in curso:
        print(letra, end='-')

    # Utilizando a função built-in range()
    # Gerando os quadrados dos números de 0 até 10
    for numero in range(1, 10, 3):
        print(numero * numero)

    lista_numeros = []

    for _ in range(6):  # 0, 1, 2, 3, 4, 5
        # O método append insert um novo item no final da lista
        lista_numeros.append(randint(1, 60))

    print(lista_numeros)

    """
    Listas em Python são tipos de dados que armazenam outros tipos de dados. Elas possuem as seguintes características:

    * Listas são iteráveis, ou seja, é possível acessar os seus valores de maneira sequencial (por exemplo, utilizando o laço for)
    * Listas são indexáveis, ou seja, é possível acessar um ou mais valores dessa lista por meio da posição (índice) desses itens
    * Listas são mutáveis, ou seja, é possível alterar um determinado valor em uma lista a partir do seu índice.
    """

    lista_palavras = ["Água", "Fogo", "Terra", "Ar"]
    palavra_da_vez = lista_palavras[randint(0, len(lista_palavras)-1)]

    texto = """
Adivinhe a palavra da vez:

1 - Água
2 - Fogo
3 - Terra
4 - Ar
"""

    print(texto)
    palavra_tentativa = int(input("Informe o número: "))
    tentativa = lista_palavras[palavra_tentativa-1]

    if tentativa == palavra_da_vez:
        print(f"Parabéns! Você acertou a palavra da vez {palavra_da_vez}.")
    else:
        print("Errou!")

    lista_palavras[3] = "Coração"
    print(lista_palavras)

    # Adicionar um novo item na lista pela posição. Utilizamos o método insert()
    lista_palavras.insert(1, "Sentimento")
    print(lista_palavras)

    # Podemos remover itens de uma lista, utilizando o método pop()
    lista_palavras.pop()
    lista_palavras.pop(2)

    # Utilizando o método remove()
    lista_palavras.remove("Água")

    # Utilizando a palavra reservada del
    del lista_palavras[1]

    print(lista_palavras)

    # Cópia de listas

    # A linha abaixo irá causar um comportamento estranho, pois a alteração de uma lista refletirá na outra
    # nova_lista_palavras = lista_palavras

    # Para fazer corretamente a cópia de listas, podemos utilizar 2 métodos:

    # 1. O método copy()
    # nova_lista_palavras = lista_palavras.copy()

    # 2. Utilizar slicing(fatiamento) de listas
    nova_lista_palavras = lista_palavras[:]

    nova_lista_palavras.append("Felicidade")
    nova_lista_palavras.extend(["Solidão", "Carinho"])

    print(nova_lista_palavras)

    print(nova_lista_palavras[1:3])
    