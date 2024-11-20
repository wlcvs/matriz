from typing import List, Union
import elemento

class Matriz:
    def __init__(self, qtd_linhas_m: Union[int, None], qtd_colunas_n:Union[int, None]):
        self.qtd_linhas_m = qtd_linhas_m
        self.qtd_colunas_n = qtd_colunas_n
        self._elementos: List[Elemento] = []

        self._linhas = []
        self._colunas = []

    def add_elemento(self, linha_m: int, coluna_n: int, valor: Union[float, None]) -> None:
        pass

    def del_elemento(self, linha_m: int, coluna_n: int) -> None:
        pass

