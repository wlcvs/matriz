from typing import Union

class Elemento:
    def __init__(self, linha_m: int, coluna_n: int, valor: Union[float, None]):
        self._linha_m = linha_m
        self._coluna_n = coluna_n
        self._valor = valor

    def __str__(self):
        return str(self._valor)

