"""
Entrada e saída (I/O) de arquivos em Python

Leitura de arquivos .txt

"""

if __name__ == "__main__":
    
    """
    A função built-in open() abre um arquivo. O único argumento obrigatório dessa função é o nome/caminho do arquivo. Também podemos informar o modo de abertura desse arquivo. No Python, existem 4 modos de abertura:
    r -> Modo somente leitura (padrão)
    w -> Modo somente escrita (Sobrescrevendo o arquivo) (write)
    x -> Somente criação do arquivo
    a -> Modo de escrita (Escrevendo a partir do fim do arquivo)
    
    """
    arquivo = open("mercado.txt")
    print(arquivo.read())
    arquivo.close()

    arquivo = open(file="mercado.txt", mode='r', encoding="utf-8")

    # O método read() lê o conteúdo do arquivo como string. Podemos informar a quantidade de bytes (caracteres) que queremos ler
    print(arquivo.read(3))

    # O método readline lê o conteúdo de uma linha
    print(arquivo.readline())

    # Caso informemos um valor, ele vai ler na linha atual a quantidade de caracteres informada, não importando se são menos caracteres
    print(arquivo.readline(2))
    print(arquivo.readline(10))

    # O método readlines retorna uma lista com os itens sendo as linhas. Caso informemos algum valor, ele vai retornar a linha completa de onde parou o cursor.
    print(arquivo.readlines(7))
    print(arquivo.readlines())

    # Como o cursor está no final do arquivo, nada mais será exibido
    print(arquivo.read())

    # O método tell() retorna a posição atual do cursor no arquivo
    print(arquivo.tell())

    # O método seek() move o cursor no arquivo. Como passamos apenas 1 parâmetro, ele vai mover o cursor com base no início do arquivo
    arquivo.seek(0)

    print(arquivo.readlines())