
  

## Algoritmo de Huffman:

  

1.  **Contagem de frequência:** Primeiro, você precisa calcular a frequência de cada símbolo no texto que deseja codificar. Isso pode ser feito contando a ocorrência de cada símbolo no texto.

2.  **Construção da árvore de Huffman:** Em seguida, você constrói uma árvore de Huffman usando essas frequências. A ideia é que os símbolos menos frequentes estejam mais distantes da raiz da árvore, enquanto os mais frequentes estejam mais próximos da raiz.

3.  **Atribuição de códigos:** Atribui-se um código binário único para cada símbolo, seguindo o caminho da raiz até o nó folha na árvore de Huffman. Os símbolos mais frequentes terão códigos mais curtos.

  

## Algoritmo Guloso para Código de Huffman:

  

A abordagem gulosa é uma maneira eficiente de construir a árvore de Huffman. Aqui está como funciona:

  

1.  **Inicialização:** Inicie com uma fila de prioridade contendo todos os símbolos e suas frequências, ordenados pela frequência.

2.  **Construção da árvore:** Repetidamente, remova os dois símbolos de menor frequência da fila de prioridade, crie um novo nó pai com esses dois símbolos como filhos e adicione o novo nó de volta à fila de prioridade com sua frequência sendo a soma das frequências dos filhos.

3.  **Até restar apenas um nó:** Continue esse processo até que apenas um nó permaneça na fila de prioridade. Este nó será a raiz da árvore de Huffman.

4.  **Atribuição de códigos:** Atribua os códigos binários aos símbolos seguindo o caminho da raiz até o nó folha.

  
  

## Explicação do Código

Este código implementa o algoritmo de codificação de Huffman, que é um método de compressão de dados que utiliza códigos de comprimento variável para representar símbolos diferentes. Vou explicar como funciona:

  

1.  **Classe Node:**

- Define um nó da árvore de Huffman.

- Cada nó tem um símbolo associado (para folhas da árvore) e uma frequência.

- Também possui referências para os filhos esquerdo e direito.

2.  **Função build_huffman_tree:**

- Cria uma fila de prioridade (PriorityQueue) e adiciona todos os símbolos com suas frequências como nós individuais na fila.

- Em seguida, enquanto houver mais de um nó na fila, ele retira os dois nós com as menores frequências, cria um novo nó pai com a soma das frequências desses dois nós e os torna filhos deste nó pai.

- Esse processo continua até que haja apenas um nó na fila, que se torna a raiz da árvore de Huffman.

3.  **Função huffman_codes:**

- Percorre recursivamente a árvore de Huffman.

- Quando alcança um nó folha, armazena o código Huffman (caminho da raiz até o nó) associado a esse símbolo em um dicionário.

4.  **Função huffman_encoding:**

- Chama a função build_huffman_tree para criar a árvore de Huffman.

- Em seguida, chama a função huffman_codes para gerar os códigos Huffman para cada símbolo.

- Finalmente, codifica o texto original substituindo cada símbolo pelo seu código Huffman correspondente.

5.  **Exemplo de uso:**

- Define uma lista de símbolos e suas frequências.

- Chama huffman_encoding para obter o texto codificado e o dicionário de códigos de Huffman.

- Imprime os resultados.
