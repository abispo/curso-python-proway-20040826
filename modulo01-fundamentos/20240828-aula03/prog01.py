"""
Funções (Procedures)

Funções são blocos de código que podem ser chamados em qualquer lugar do nosso programa. As funções podem receber valores a partir de parâmetros e também retornar valores. Funções também são consideradas objetos dentro do Python.

Para criar uma função, utilizamos a palavra reservada def
"""

from datetime import datetime

# Função sem parâmetros e sem retorno
def ola():
    print("Olá Python")

# Função que não recebe parâmetros, e que retorna um valor
def hora_certa():
    return datetime.now()

# Função que possui parâmetros, e que retorna um valor
def calculo_imc(altura: float, peso: float):
    return peso / (altura * altura)

def calculo_salario(
        valor: float, multiplicador: float, adicional: float = 0
    ):
    return (valor * multiplicador) + adicional

if __name__ == "__main__":

    ola()
    print(ola())

    agora = hora_certa()
    print(agora)

    altura = float(input("Informe sua altura em metros (ex: 1.76): "))
    peso = float(input("Informe o seu peso em Kg (ex: 85.6): "))

    # Aqui, estamos passando os valores para a função de maneira posicional, ou seja, estamos passando de acordo com a posição do parâmetro
    imc = calculo_imc(altura, peso)
    print(f"Altura: {altura} | Peso: {peso} | IMC: {imc:.1f}")

    # Também podemos passar os valores para a função pelo nome dos parâmetros, ou, keywords. Por exemplo:
    imc = calculo_imc(altura=1.97, peso=98)
    print(f"Altura: 1.97 | Peso: 98 | IMC: {imc:.1f}")

    # Dessa maneira,não importa a ordem que passamos os valores.
    imc = calculo_imc(peso=100.5, altura=1.85)
    print(f"Altura: 1.85 | Peso: 100.5 | IMC: {imc:.1f}")

    valor_final = calculo_salario(1000, 1.1)
    print(f"Salário: 1000 | Multiplicador: 1.1 | Adicional: 0 | Total: {valor_final}.")

    valor_final = calculo_salario(2500, 1.2, 500)
    print(f"Salário: 2500 | Multiplicador: 1.2 | Adicional: 500 | Total: {valor_final}.")

    valor, multiplicador, adicional = 1800, 1.2, 200

    valor_final = calculo_salario(
        multiplicador=multiplicador,
        valor=valor,
        adicional=adicional
    )
    print(f"Salário: {valor} | Multiplicador: {multiplicador} | Adicional: {adicional} | Total: {valor_final}.")

    # O código abaixo não irá funcionar, pois o Python proíbe que os valores dos argumentos passados via posição, apareçam depois dos valores dos argumentos passador por nome
    # valor = calculo_salario(adicional=100, 1500, 1.1)