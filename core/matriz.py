from typing import List, Union
import elemento

class Matriz:
    def __init__(self, qtd_linhas_m: int, qtd_colunas_n: int):
        self.qtd_linhas_m = qtd_linhas_m
        self.qtd_colunas_n = qtd_colunas_n
        self._elementos: List[Elemento] = []

    def add_elemento(self, linha_m: int, coluna_n: int, valor: Union[float, None]) -> None:
        if linha_m <= self.qtd_linhas_m:
            if coluna_n <= self.qtd_colunas_n:
                self._elementos.add(Elemento(linha_m, coluna_n, valor))
            else:
                raise ValueError("O valor fornecido para a coluna do elemento está fora dos limites da matriz")
        else:
            raise ValueError("O valor fornecido para linha do elemento está fora dos limites da matriz")



