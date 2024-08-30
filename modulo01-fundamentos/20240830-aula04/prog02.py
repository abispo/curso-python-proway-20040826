"""
Trabalhando com arquivos .csv no Python

Lendo arquivos .csv com reader e DictReader
"""

import csv
import os

if __name__ == "__main__":

    caminho_arquivo = os.path.join(os.getcwd(), "arquivos", "clientes.csv")

    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:

        # Aqui criamos um objeto representando um arquivo csv. Como os valores no nosso arquivo csv são separados por ponto-e-vírgula, e não apenas por vírgula(padrão), precisamos indicar isso na chamada do método, passando o parâmetro delimiter
        arquivo_csv = csv.reader(arquivo, delimiter=';')

        for linha in arquivo_csv:
            print(linha[2])

    # ----------------------------------------------------------------------

    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:

        arquivo_csv = csv.DictReader(arquivo, delimiter=';')

        print("*** CLIENTES ***")
        print('*'*17)

        for linha in arquivo_csv:
            saida = """
Nome: {nome},
Idade: {idade},
valor: {valor}
""".format(**linha)
            
            print(saida)
            print('*'*50)