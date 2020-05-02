"""
Primeiro Excercício: Utilizando um dicionário
Apresentar quais são caracteres de uma string e contar quantas vezes cada caracter aparece na mesma
"""

def contar_caracteres(s):
    """ Função que conta os caracteres de um dicionário
    Ex:
        >>> contar_caracteres('walter')
        {'a': 1, 'e': 1, 'l': 1, 'r': 1, 't': 1, 'w': 1}

        >>> contar_caracteres('banana')
        {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada
    :return:
    """
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    resultado = {}

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            resultado[caracter_anterior] = contagem
            caracter_anterior = caracter
            contagem = 1
    resultado[caracter_anterior] = contagem

    return resultado


if __name__ == '__main__':
    print(contar_caracteres('walter'))
    print()
    print(contar_caracteres('banana'))
