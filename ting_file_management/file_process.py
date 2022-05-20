"""
Requisito 3: Passos a se seguir:
1 - A função process lê o arquivo que é carregado na questão anterior
    e efetua o processamento do conteúdo
2 - A função receb como parâmetro o caminho do arquivo e a instância da fila
    do requisito 1 (ou seja, é possível acessar seus métodos)
3 - ignorar arquivos com caminhos já processados anteriormente
4 - Retornar:
    {
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [...]
    }

Lógica a se pensar:
1 - a instância recebida como parâmetro retorna uma lista (fila) de linhas,
    com isso, podemos percorrê-la
2 - Caso o arquivo possua o nome igual ao caminho que foi passado no parâmetro
    retornar nulo
3 - Chamar a função txt_importer passando o path_file como parâmetro, assim
    o retorno que é a lista pode ser usado nos dados que serão renderizados
4 - Crior o objeto que vai ter a string com os dados formatados.
5 - Adicionar essa string no método enqueue da instância, para adionar à lista
6 - Imprimir no terminal usando o stdout

Requisito 4: Passos a se seguir:
1 - A função recebe como parâmetro a fila criada no requisito 1
2 - Caso não existam arquivos na fila, retornar via stdout 'Não há elementos'
3 - Caso tenha sucesso, emitir via stdout:
    'Arquivo {path_file} removido com sucesso'

Lógica a se pensar:
1 - Veririficar se o tamanho da lista é igual a 0, se for retornar a mensagem
    "Não há elementos"
"""
from .file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    response = txt_importer(path_file)
    string_response = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(response),
        "linhas_do_arquivo": response,
    }
    instance.enqueue(string_response)
    sys.stdout.write(str(string_response))


def remove(instance):
    length_list = instance.__len__()
    if length_list == 0:
        return sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
