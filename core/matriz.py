from typing import List, Union
from elemento import Elemento

class Matriz:
    def __init__(self, qtd_linhas_m: Union[int, None], qtd_colunas_n:Union[int, None]):
        self.qtd_linhas_m = qtd_linhas_m
        self.qtd_colunas_n = qtd_colunas_n
        self._elementos: List[Elemento] = []

    def add_elemento(self, linha_m: int, coluna_n: int, valor: Union[float, None]) -> None:
        if len(self._elementos) > 1:
            for i in range(len(self._elementos)):
                elemento = self._elementos[i]
                if elemento._linha_m == linha_m and elemento._coluna_n == coluna_n:
                    raise ValueError(f"Já existe um elemento nesta posição, linha: {linha_m} coluna: {coluna_n}")
                    return
        if self.qtd_linhas_m and self.qtd_colunas_n:
            if linha_m <= self.qtd_linhas_m:
                if coluna_n <= self.qtd_colunas_n:
                    self._elementos.append(Elemento(linha_m, coluna_n, valor))
            else:
                self._elementos.append(Elemento(linha_m, coluna_n, valor))

    def bubble_sort(self):
        tamanho_lista = len(self._elementos)
        for i in range(tamanho_lista):
            for j in range(0, tamanho_lista - i - 1):
                if self._elementos[j].linha_m > self._elementos[j + 1].linha_m:
                    self._elementos[j], self._elementos[j + 1] = self._elementos[j + 1], self._elementos[j]
                if self._elememtos[j].coluna_n > self._elementos[j + 1].coluna_n:
                    self._elementos[j], self._elementos[j + 1] = self._elementos[j + 1], self._elementos[j]

    def visualizar(self):
        # Criação da estrutura de dados
        matriz = []
        for i in range(self.qtd_linhas_m):
            matriz.append([]) # inserção das linhas
            for j in range(self.qtd_colunas_n):
                matriz[i].append([0]) # inserção das colunas
        # Preenchimento com os valores reais 
        for i in range(len(self._elementos)):
            for j in range(1, self.qtd_linhas_m + 1):
                for k in range(1, self.qtd_colunas_n + 1): 
                    if self._elementos[i]._linha_m == j and self._elementos[i]._coluna_n == k: 
                        matriz[j - 1][k - 1] = [self._elementos[i]._valor] 
        # Exibição da matriz de fato
        matriz_str = str(matriz)
        matriz_list = list(matriz_str)
        colchetes = ["["]
        for i in range(len(matriz)):
            

'''
[0, 0]
[0, 0]
'''
matriz_1 = Matriz(2, 2)

'''
[0, 9.0]
[0, 0]
'''
matriz_1.add_elemento(1, 2, 9.0)

'''
[0, 9.0]
[0, 170.0]
'''
matriz_1.add_elemento(2, 2, 170.0)

'''
[0, 9.0]
[-1.0, 170.0]
'''
matriz_1.add_elemento(2, 1, -1.0)

# isso tem que dar erro
# matriz_1.add_elemento(1, 2, -1.0)

matriz_1.visualizar()
