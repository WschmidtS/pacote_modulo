"""
Primeiro Excercício: Utilizando um dicionário
Apresentar quais são caracteres de uma string e contar quantas vezes cada caracter aparece na mesma
"""

def contar_caracteres(s):
    """ Função que conta os caracteres de um dicionário
      Ex:
          >>> contar_caracteres('walter')
          {'w': 1, 'a': 1, 'l': 1, 't': 1, 'e': 1, 'r': 1}
          >>> contar_caracteres('banana')
          {'b': 1, 'a': 3, 'n': 2}

      :param s: string a ser contada
      :return:
      """

    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado


if __name__ == '__main__':
    print(contar_caracteres('walter'))
    print()
    print(contar_caracteres('banana'))