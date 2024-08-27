# Exercícios (Loops, listas e dicionários)

1. Escreva um programa que receba um número maior do que 1 pelo terminal. Em seguida, o programa retorna a soma de 1 até esse número. Ex:

```
Informe o número: 5
A soma de 1 até 5 é 15
```

2. Escreva um programa que receba números pelo terminal. Se o usuário digitar o número 0, o programa para de receber números pelo terminal e retorna uma lista dos quadrados desses números. Exemplo:

```
Digite um número: 4
Digite um número: 2
Digite um número: 6
Digite um número: 0

Lista dos quadrados: [16, 4, 36]
```

3. Escreva um programa que gere 100 números randômicos de 1 a 100. Em seguida, crie 2 listas: Uma que irá salvar apenas os números pares, e outra que irá salvar apenas os números ímpares. Em seguida, mostre na tela a quantidade de itens de cada lista e quais são os seus valores. Exemplo:

```
Itens na lista de pares: 5
Valores: [2, 8, 20, 50, 4]

Itens na lista de ímpares: 4
lista_impares = [45, 79, 3]
```

4. Escreva um programa que converta uma lista de inteiros em apenas 1 inteiro. Exemplo:

```
lista = [4, 7, 10, 24]
Saída: 471024
```

5. Escreva um programa que gere números randômicos de 0 até 50. Salve esse números em uma lista. Em seguida, informe quais são o maior e o menor número dessa lista. Dica: Utilize as funções built-in `max()` e `min()`

6. Escreva um programa que imprima o seguinte padrão no terminal:

```
#
##
###
####
#####
```

7. Escreva um programa que receba nome, idade e sexo de 5 usuários. Em seguida, mostre quantos usuários são do sexo masculino, quantos são do sexo feminino e qual é a média de idade. Exemplo:

```
Nome: João
Idade: 32
Sexo: M

Nome: Maria
Idade: 17
Sexo: F

Nome: Vanessa
Idade: 28
Sexo: F

Quantidade de usuários do sexo masculino: 1
Quantidade de usuários do sexo feminino: 2
Média de idade: 25.67
```

8. Escreva um programa em Python que inverta uma lista de números. Exemplo:

```
lista = [4, 7, 8, 1, 9]
lista_invertida = [9, 1, 8, 7, 4]
```

9. Escreva um programa em Python que gere uma lista randômica de 50 números de 1 até 50. Em seguida, retire os valores repetidos dessa lista (utilize a função `randint()` do pacote `random`)

# Exercícios funções

1. Escreva uma função em Python que informe uma quantidade arbitrária de argumentos do tipo inteiro, e retorne a soma desses valores.

2. Escreva uma função em Python que receba 3 parâmetros: inicio, fim e numero. A função deve retornar True se o numero estiver entre inicio e fim

3. Escreva uma função que receba uma lista, e retorne a mesma lista, porém sem valores repetidos

4. Crie uma função que receba 2 argumentos: base e expoente. Essa função vai retornar o
   resultado da base elevado ao expoente. Se o valor do expoente não for informado, a função
   deve considerar que o valor é 2

5. Crie uma função que receba uma lista de inteiros como argumento. Essa função deve retornar o item que mais aparece na lista e quantas vezes ele aparece

6. Crie uma função que calcule a média de valores informados. A função receberá uma lista com 5 valores, e pra calcular a média vai ignorar o maior e o menor valor.

7. Crie uma função chamada cadastrar_cliente que receba as informações dos clientes usando `*args` e `**kwargs`. A função deve armazenar os dados dos clientes em um dicionário e exibir os dados cadastrados.

8. Você tem uma lista de dicionários, onde cada dicionário representa um produto em uma loja. Cada produto tem um nome, um preço e uma quantidade em estoque. Seu objetivo é utilizar funções lambda para filtrar os produtos com base em certos critérios e ordená-los.
