"""
Entrada e saída (I/O) de arquivos em Python

Escrita de arquivos .txt
"""

import os

if __name__ == "__main__":

    pasta = "arquivos"
    caminho_pasta = os.path.join(os.getcwd(), pasta)

    arquivo_linguagens = os.path.join(caminho_pasta, "linguagens.txt")

    if not os.path.exists(pasta):
        os.mkdir(caminho_pasta)

    with open(arquivo_linguagens, "w", encoding="utf-8") as arquivo:
        for index in range(1, 4):

            linguagem = input("Informe uma linguagem de programação que você conheça: ")

            arquivo.write(f"{linguagem}\n")

    with open(arquivo_linguagens, "a", encoding="utf-8") as arquivo:
        lista_linguagens = [
            "Scala\n", "Rust\n", "Golang\n"
        ]
        arquivo.writelines(lista_linguagens)

