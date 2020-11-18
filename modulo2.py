import re

patron = re.compile("[A-Za-z]+(?:[ _-][A-Za-z]+)*$")


def valida(texto):
    if patron.match(texto) == None:
        return True