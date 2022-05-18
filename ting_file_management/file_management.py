"""
Requisito 2: Passos a se seguir:
1 - A função file_management importa dados de um arquivo txt
2 - Utiliza \n como separador
3 - As mensagens de erro devem ir para a stderr
4 - Caso o arquivo TXT não exista, deve exibir a mensagem
    'Arquivo {path_file} não encontrado'
5 - Caso a extensão seja diferente de txt, retornar o erro 'Formato inválido'
6 - Retornar uma lista com as linhas do arquivo

Lógica a se pensar:
1 - Verificar primeiro se o arquivo termina com formato txt, caso não
    retornar erro na stderr com 'Formato inválido'
2 - Fazer a leitura do arquivo, convertando cada linha em um valor de lista
3 - Cada valor da lista é obtido separando o texto onde a linha quebra.
    Para isso, usar o split('\n')
4 - Caso não exista um arquivo, fazer um except de FileNotFoundError
    retornando a mensagem 'Arquivo {path_file} não encontrado' no terminal
"""
import sys


def txt_importer(path_file):
    if not path_file.endswith('txt'):
        return sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file, mode="r") as data:
            list_data = data.read().split('\n')
            return list_data
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
