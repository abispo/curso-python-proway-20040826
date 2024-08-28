"""
Laços de condição

Laço while

O laço while é utilizado quando precisamos executar um bloco de código repetidas vezes, enquanto uma determinada condição é verdadeira.
"""

from random import randint
from time import sleep

if __name__ == "__main__":

    """
    Dicionário

    Um Dicionário é um outro tipo de dado que temos em Python, que é caracterizado pelo seu formato chave: valor. Exemplo:

    dados = {
        "nome": "Maria",
        "curso": "Java",
        10: "chave numerica",
        1.2: [1, 2, 3]
        "info": {
            "horario": 1,
            "preco": 80
        }
    }

    Como vimos, não podemos ter qualquer tipo de dado como chave em um dicionário (apenas os tipos "primitivos"), porém podemos ter qualquer tipo de dado como valor associado a essa chave.

    Assim como listas, dicionários são:

        * Iteráveis
        * Indexáveis
        * Mutáveis
    """

    # Motor de Batalha!

    heroi = {
        "nome": "Gimli",
        "att": 12,
        "def": 10,
        "hp": 25,
    }

    monstro = {
        "nome": "Orc",
        "att": 13,
        "def": 10,
        "hp": 16
    }

    print("=== Arena de Batalha! ===")
    print("= Participantes =")
    print('-'*50)

    for index, personagem in enumerate([heroi, monstro], 1):
        print(f"= Combatente {index} =")
        for chave, valor in personagem.items():
            print(f"{chave}: {valor}")

        print('-'*30)

    batalha_acontecendo = True
    vencedor = None

    while batalha_acontecendo:
        
        print(f"{heroi['nome']} ataca {monstro['nome']}!")
        dado = randint(1, 6)

        ataque_heroi = heroi['att'] + dado

        if ataque_heroi > monstro['def']:
            monstro['hp'] -= (ataque_heroi - monstro['def'])
        else:
            print(f"{monstro['nome']} defendeu o ataque!")

        if monstro['hp'] <= 0:
            vencedor = heroi
            batalha_acontecendo = False
            continue

        sleep(1.5)
        # -------- Ação do monstro ---------

        print(f"{monstro['nome']} ataca {heroi['nome']}!")
        dado = randint(1, 6)

        ataque_monstro = monstro['att'] + dado

        if ataque_monstro > heroi['def']:
            heroi['hp'] -= (ataque_monstro - heroi['def'])
        else:
            print(f"{heroi['nome']} defendeu o ataque!")

        if heroi['hp'] <= 0:
            vencedor = monstro
            batalha_acontecendo = False
            continue

    # teste = vencedor.copy()
    # teste.pop("nome")

    print("Vencedor da batalha:")
    print(f"Nome: {vencedor['nome']}")
    print(f"Saiu vivo com {vencedor['hp']}hp.")