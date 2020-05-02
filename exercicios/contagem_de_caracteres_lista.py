"""
Primeiro Excercício: Utilizando uma lista
Apresentar quais são caracteres de uma string e contar quantas vezes cada caracter aparece na mesma
"""

def contar_caracteres(s):
    """ Função que conta os caracteres de uma string
    Ex:
        >>> contar_caracteres('walter')
        a:1
        e:1
        l:1
        r:1
        t:1
        w:1
        >>> contar_caracteres('banana')
        a:3
        b:1
        n:2

    :param s: string a ser contada
    :return:
    """
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}:{contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}:{contagem}')

if __name__ == '__main__':
    contar_caracteres('walter')
    print()
    contar_caracteres('banana')