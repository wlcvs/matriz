from typing import List, Union
from elemento import Elemento

class Matriz:
    def __init__(self, qtd_linhas_m: Union[int, None], qtd_colunas_n:Union[int, None]):
        self.qtd_linhas_m = qtd_linhas_m
        self.qtd_colunas_n = qtd_colunas_n
        self._elementos: List[Elemento] = []

    def add_elemento(self, linha_m: int, coluna_n: int, valor: Union[float, None]) -> None:
        if self.qtd_linhas_m and self.qtd_colunas_n:
            if linha_m <= self.qtd_linhas_m:
                if coluna_n <= self.qtd_colunas_n:
                    self._elementos.append(Elemento(linha_m, coluna_n, valor))
        else:
            self._elementos.append(Elemento(linha_m, coluna_n, valor))


