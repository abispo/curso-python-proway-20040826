"""
Funções (procedures)

Funções lambda

Existe a possibilidade de criarmos funções anônimas (funções que não possuem nome definido) dentro do Python. Chamamos essas funções de funções lambda.
"""

from typing import Dict


def esta_aprovado(aluno: Dict[str, str | float]) -> bool:
    return aluno.get("nota_final") >= 7
    

if __name__ == "__main__":
    
    funcao_anonima = lambda: 10 * 10
    print(funcao_anonima())

    funcao_anonima_2 = lambda a, b: a * b
    print(funcao_anonima_2(5, 15))

    lista_alunos = [
        {"nome": "Maria", "nota_final": 8.0},
        {"nome": "João", "nota_final": 5.5},
        {"nome": "Carlos", "nota_final": 3.5},
        {"nome": "Paulo", "nota_final": 9.0},
        {"nome": "Renata", "nota_final": 10.0}
    ]

    for aluno in lista_alunos:
        if esta_aprovado(aluno):
            print("O aluno {nome} está aprovado com a nota {nota_final}".format(
                **aluno
            ))

    # Pegando a lista dos alunos aprovados utilizando filter()
    lista_aprovados = list(filter(esta_aprovado, lista_alunos))
    print(lista_aprovados)

    # Agora utilizando uma função anônima (lambda)
    lista_reprovados = list(filter(
        lambda x: x.get("nota_final") < 5, lista_alunos
    ))
    print(lista_reprovados)

    lista_quadrados = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))
    print(lista_quadrados)
