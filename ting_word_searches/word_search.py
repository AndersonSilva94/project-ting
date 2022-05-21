"""
Requisito 6: Passos a se seguir:
1 - A função exists_word recebe como parâmetro a instância da lista do req 1
    e uma palavra que será usada para buscar sua existência na lista
2 - Para cada vez que a palavra é encontrada, deve exibir sua linha
3 - Caso a palavra não seja encontrada em nenhum arquivo, retornar uma lista
    vazia
4 - A busca deve ser case insensitive e retornar:
    [{
      "palavra": "de",
      "arquivo": "arquivo_teste.txt",
      "ocorrencias": [
        {
          "linha": 1
        },
        {
          "linha": 2
        }
      ]
    }]
5 - A fila não pode ser modificada durante a busca

Lógica a se pensar:
1 - Criar três variáveis que vão armazenar: o retorno formatado do resultado,
    os valores de qual linha foram encontrados e a linha em si
2 - fazer um for na lista trazida na instância e em seguida, um novo for
    na propriedade 'linhas_do_arquivo' para recuperar os textos existentes
3 - Verificar se a palavra faz parte do texto da linha (ambos em minúsculo)
    Caso sim, adiocionar {'linha': valor_da_linha}
4 - Caso não seja encontrado nenhum texto com a palavra, retornar lista vazia
5 - Caso tenha dados, retornar no formato pedido na questão, em forma de
    lista
"""


def exists_word(word, instance):
    list_result = list()
    ocurrencies = list()
    word_converted = word.lower()
    for element in instance.line:
        line_value = 0
        for text in element['linhas_do_arquivo']:
            line_value += 1
            if word_converted in text.lower():
                ocurrencies.append({"linha": line_value})
        if len(ocurrencies) == 0:
            return ocurrencies
        response = {
            "palavra": word.lower(),
            "arquivo": element['nome_do_arquivo'],
            "ocorrencias": ocurrencies
        }
        list_result.append(response)
    return list_result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
