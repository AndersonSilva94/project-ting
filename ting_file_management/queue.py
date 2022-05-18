"""
Requisito 1: Passos a se seguir:
1 - A fila (Queue) deve ser uma estrutura FIFO (primeiro a entrar, primeiro
    a sair)
2 - Implementar os métodos de inserção (enqueue), remoção (dequeue) e
    busca (search)
3 - Implementar o método que retorna o tamanho da fila (__len__)
4 - Caso tenha um índice inválido nos parâmetros da busca, retornar um
    except IndexError. (São válidos índices inteiros entre 0 e N-1)

Lógica a se pensar:
1 - Criar uma lista como atributo da classe e armazenar os valores da fila
2 - Verificar seu tamanho com len(list)
3 - Para adicionar um novo valor na lista, usar o append()
4 - O dado há mais tempo na fila é o primeiro que entrou, para removê-lo
    utilizar pop() passando o índice que será removido
5 - Para retornar o elemento filtrado é necessário verificar se o índice
    passado é válido, ou seja, se ele é inteiro e é maior que 0 e menor que
    o tamanho da lista. Caso não seja retornar o IndexError
    Do contrário, retornar o elemento que está na posição passada por
    parâmetro
"""


class Queue:
    def __init__(self):
        self.line = list()

    def __len__(self):
        return len(self.line)

    def enqueue(self, value):
        return self.line.append(value)

    def dequeue(self):
        return self.line.pop(0)

    def search(self, index):
        if index < 0 or index > len(self.line):
            raise IndexError
        return self.line[index]
