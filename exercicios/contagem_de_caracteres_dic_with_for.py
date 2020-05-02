"""
Primeiro Excercício: Utilizando um dicionário
Apresentar quais são caracteres de uma string e contar quantas vezes cada caracter aparece na mesma
"""

def contar_caracteres(s):
    """ Função para contar os caracteres de um dicionário utilizando o for
    Ex.
    >>>contar_caracteres('walter')
   {'w': 1, 'a': 1, 'l': 1, 't': 1, 'e': 1, 'r': 1}
   >>>contar_caracteres('banana')
    {'b': 1, 'a': 3, 'n': 2}
    :para s: string a ser contata
    """
    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter] = contagem
    return resultado


if __name__ == '__main__':
    print(contar_caracteres('walter'))
    print()
    print(contar_caracteres('banana'))