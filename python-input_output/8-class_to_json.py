#!/usr/bin/python3
"""
function is declared
"""


def class_to_json(obj):
    """
    class to json
    """
    content = obj.__dict__
    dic = {
        clave: valor
        for clave, valor in content.items()
        if isinstance(valor, (list, dict, str, int, bool))
    }
    return dic
