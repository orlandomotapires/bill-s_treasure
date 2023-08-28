# Encontre o Tesouro de Bill

Este é um desafio de programação proposto pelo professor Dr. José Grimaldo da Silva Filho. Sua missão é ajudar Bill a encontrar o seu tesouro em um terreno 10x10, mas com um desafio adicional: você não pode utilizar algoritmos que façam uso de memória, tais como DFS, BFS, Dijkstra ou A*.

## Descrição

Bill perdeu seu tesouro em um terreno de 10x10 metros e ele conta com a sua sagacidade para resgatá-lo. No entanto, existem algumas restrições a serem consideradas:
- A utilização de algoritmos que utilizem memória está proibida.
- Você começa escolhendo um ponto (x, y) no grid como ponto de partida.
- Você pode mover Bill apenas para cima, para baixo, para a esquerda ou para a direita.
- O tesouro está escondido em algum lugar aleatório no grid.
- Você possui um laser que indica a distância euclidiana de cada casa ao redor de Bill até o tesouro. Você pode usar esse laser!

Sua tarefa é criar um algoritmo eficiente que encontre o tesouro de Bill o mais rápido possível, aderindo às regras mencionadas acima.

**Observação:** Para obter informações mais detalhadas sobre o problema proposto, consulte o arquivo `BillExercise.odt.pdf` fornecido pelo Professor Grimaldo.

## Instalação das Dependências

Antes de começar, certifique-se de ter instalado as seguintes dependências Python:

1. Nenhum pacote de terceiros é necessário para este desafio, pois ele utiliza apenas as bibliotecas padrão do Python.

Você pode seguir as etapas abaixo para verificar se as dependências necessárias estão presentes:

```bash
# Verifique se o Python está instalado
python --version

# Verifique se o pacote tkinter está disponível (biblioteca GUI do Python)
python -m tkinter -h
```

Caso o tkinter não esteja já instalado, o comando `sudo apt install python3-tk` (para o Linux) deve resolver.

## Como usar

O algoritmo presente no arquivo `bill_found_the_treasure.py` já está desenvolvido com uma lógica simplória que desenvolvemos, edite o `bill_temp.py` para realizar sua própria solução!

1. Clone este repositório para o seu ambiente local.
2. Implemente a lógica para encontrar o tesouro no arquivo `bill_temp.py`.
3. Execute o arquivo para verificar se você encontrou o tesouro corretamente.
