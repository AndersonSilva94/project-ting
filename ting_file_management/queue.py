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
"""


class Queue:
    def __init__(self):
        self.line = list()

    def __len__(self):
        return len(self.line)

    def enqueue(self, value):
        return self.line.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""

    def search(self, index):
        """Aqui irá sua implementação"""
