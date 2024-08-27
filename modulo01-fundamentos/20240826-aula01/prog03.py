"""
Programa que calcula a média de um aluno
"""

if __name__ == "__main__":

    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media < 5:
        print("Você foi reprovado. Média: {:.1f}".format(media))

    elif media >= 5 and media < 7:
        print(f"Você está de recuperação. Média {media:.1f}")

    else:
        print(f"Você foi aprovado. Média: {media:.1f}")
