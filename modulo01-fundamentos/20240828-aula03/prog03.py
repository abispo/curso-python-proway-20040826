"""
Funções (Procedures)

Funções recursivas

Função recursiva é uma função que chama a si mesma. Temos a função matemática fatorial, como um exemplo clássico de recursão
"""

# 5! -> 5 * 4 * 3 * 2 * 1

def fatorial_nao_recursivo(numero: int):
    contador = numero
    total = numero

    while contador > 1:
        total = total * (contador - 1)
        contador = contador - 1

    return total

def fatorial_recursivo(numero: int):
    if numero == 1:
        return numero
    
    return numero * fatorial_recursivo(numero - 1)

if __name__ == "__main__":
    
    print("Fatorial não recursivo de 5: {}".format(
        fatorial_nao_recursivo(5)
    ))

    print("Fatorial recursivo de 5: {}".format(
        fatorial_recursivo(5)
    ))
