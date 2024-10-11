# Projetos Python  
Repositório com alguns projetos feitos na linguagem python  

## Biblioteca  
O programa simula um sistema de biblioteca, onde livros podem ser emprestados e devolvidos. Ele possui duas classes principais:

- **Biblioteca:** Gerencia a disponibilidade de livros. Possui métodos para mostrar livros disponíveis, emprestar e devolver livros.  
- **Estudante:** Representa um estudante que pode pegar emprestado ou devolver livros da biblioteca. Ele mantém uma lista de livros que o estudante emprestou.
  
O sistema permite que o usuário interaja por meio de um menu simples com as opções de exibir os livros disponíveis, pegar emprestado um livro, devolver um livro e visualizar os livros emprestados pelo estudante.

É um exemplo básico de gerenciamento de empréstimos de livros utilizando Python orientado a objetos.  

## Conversor de Moedas  
O programa permite converter valores de uma moeda para outra, utilizando uma API externa para obter as taxas de câmbio atuais.  

Funcionamento:
- O usuário insere a moeda de origem (por exemplo, USD), a moeda de destino (por exemplo, EUR) e o valor a ser convertido.
- O programa utiliza a API do site apilayer para obter a taxa de câmbio atual e realizar a conversão.
- Se houver algum erro de comunicação com a API, o programa informa o problema e encerra a execução.
- O resultado da conversão é exibido ao usuário.
  
O projeto é útil para realizar conversões monetárias de forma rápida e utilizando dados atualizados.  

## Sequência Fibonacci  
O programa gera a sequência de Fibonacci até um determinado número, utilizando uma técnica de otimização chamada memoization para armazenar valores previamente calculados e evitar cálculos redundantes.  

Funcionamento: 
- O usuário insere o número desejado até o qual a sequência de Fibonacci deve ser calculada.
- A função fib_memo() utiliza um dicionário para armazenar resultados já calculados, aumentando a eficiência do algoritmo ao evitar recalcular números anteriores.
- A sequência é exibida ao usuário no formato "Fibonacci (n): resultado".
- Caso o usuário insira um valor inválido ou negativo, o programa exibe uma mensagem de erro apropriada.

## Merge Sort  
O programa implementa o algoritmo de ordenação Merge Sort, que utiliza a técnica de divisão e conquista para ordenar uma lista de números.  

Funcionamento:
- O usuário é solicitado a inserir uma lista de números inteiros, escolhendo a quantidade (entre 5 e 10) e os valores (entre 1 e 99).
- A função merge_sort() divide a lista em metades recursivamente até que cada sublista tenha apenas um elemento.
- As sublistas são então mescladas (merge) de forma ordenada, resultando em uma lista final ordenada.
- O processo de divisão e mesclagem é mostrado ao usuário por meio de mensagens impressas no console.  

O Merge Sort é um algoritmo eficiente, com complexidade de tempo O(n log n), sendo útil para ordenar grandes quantidades de dados.  

## Teste de Velocidade de Digitação  
Esse programa mede a velocidade de digitação do usuário utilizando uma interface gráfica construída com a biblioteca Tkinter.  

Funcionamento:  
- O usuário é apresentado a uma frase aleatória que deve ser digitada no campo de entrada.
- O cronômetro começa quando a frase é exibida e termina quando o usuário pressiona o botão "Feito".
- O programa compara o texto digitado com a frase original. Se a digitação estiver correta, o tempo total é exibido; caso contrário, uma mensagem de erro aparece.
- O usuário pode optar por tentar novamente, reiniciando o teste.
