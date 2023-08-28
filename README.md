# Encontre o Tesouro de Bill

Este é um desafio de programação proposto pelo professor Dr. José Grimaldo da Silva Filho, em que você ajudará o Bill a encontrar o seu tesouro em um grid 10x10, sem o uso de algoritmos que utilizem memória (DFS, BFS, Djiskstra, A*).

## Descrição

Bill perdeu seu tesouro em um terreno de 10x10 metros e precisa de sua ajuda para encontrá-lo. No entanto, existem algumas restrições:
- Você não pode usar algoritmos que façam uso de memória.
- Você pode escolher um ponto no grid (x, y) como seu ponto de partida.
- Você pode se mover apenas para cima, para baixo, para a esquerda ou para a direita.
- O tesouro está escondido em uma posição aleatória do grid.
- Você possui um laser que indica a distancia euclidiana de cada casa ao redor de Bill para o tesouro, você pode usar esse laser!

Sua tarefa é implementar um algoritmo que encontre o tesouro do Bill o mais rápido possível, seguindo as regras mencionadas acima.

Obs: O slide `BillExercise.odt.pdf` do professor Grilmando traz algumas outras informações detalhadas sobre o problema proposto.

## Como usar

O algoritmo presente no arquivo `bill_random.py` já está desenvolvido com uma lógica simplória que desenvolvemos, edite o `bill_temp.py` para realizar sua própria solução!

1. Clone este repositório para o seu ambiente local.
2. Implemente a lógica para encontrar o tesouro no arquivo `bill_temp.py`.
3. Execute o arquivo para verificar se você encontrou o tesouro corretamente.
