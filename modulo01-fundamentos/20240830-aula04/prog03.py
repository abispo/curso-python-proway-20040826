"""
Trabalhando com arquivos .csv em Python

Escrevendo arquivos .csv utilizando writer ou DictWriter
"""

import csv
import os

if __name__ == "__main__":
    
    caminho_arquivo = os.path.join(os.getcwd(), "arquivos", "compras.csv")

    lista_de_itens = [
        [1, "Banana", 12],
        [2, "Laranja", 6],
        [3, "Abacaxi", 1],
        [4, "Melancia", 1],
        [5, "Uva", 6]
    ]

    with open(caminho_arquivo, "w", encoding="utf-8", newline="") as arquivo:

        arquivo_csv = csv.writer(arquivo, delimiter=';')

        # Escrevemos a primeira linha, que é o cabeçalho do arquivo csv
        arquivo_csv.writerow([
            "id", "nome", "quantidade"
        ])

        # Escrevemos o restante das linhas utilizando o método writerows
        arquivo_csv.writerows(lista_de_itens)