from math import fabs


class GaussJordan(object):
    def __init__(self):
        self.__m = int()
        self.__n = int()

    def get_m(self):
        return self.__m

    def get_n(self):
        return self.__n

    def set_m(self, m):
        self.__m = m

    def set_n(self, n):
        self.__n = n


class GaussSeidel(object):
    def __init__(self):
        self.__k = int()
        self.__e = float()

    def get_k(self):
        return self.__k

    def get_e(self):
        return self.__e

    def set_k(self, k):
        self.__k = k

    def set_e(self, e):
        self.__e = e


class SistemaEquacoes(GaussJordan, GaussSeidel):
    def __init__(self, dim):
        self.__mat = list()
        self.__dimencao = dim
        self.__leitura_arquivos()
        self.set_m(len(self.get_mat()))
        self.set_n(self.get_m() + 1)
        self.set_k(1000)
        self.set_e(0.0000000001)

    def get_mat(self):
        return self.__mat

    def get_dimencao(self):
        return self.__dimencao

    def set_mat(self, mat):
        self.__mat = mat

    def set_dimencao(self, dimecao):
        self.__dimencao = dimecao

    def __leitura_arquivos(self):
        entrada = open(f'Entrada{self.get_dimencao()}.txt', 'r')
        linhas = ''
        mat_aux = list()
        linhas = entrada.readlines()
        for i in range(1, len(linhas) - 1):
            l = linhas[i].strip().split()
            if len(l) > 0:
                mat_aux.append(l.copy())
        l = linhas[len(linhas) - 1].strip().split()
        for i in range(0, len(mat_aux)):
            mat_aux[i].append(l[i])

        for i in range(0, len(mat_aux)):
            for j in range(0, len(mat_aux) + 1):
                mat_aux[i][j] = int(mat_aux[i][j])
        self.set_mat(mat_aux)

    def __escrita_arquivos(self):
        saida = open('Saida.txt', 'w')
        saida.write(f'Sistema de dimencao {self.get_m()}: ')
        for i in range(len(self.__mat)):
            saida.write(str(self.__mat[i][self.get_n() - 1]) + ' ')
        saida.write('\n')

    def pivotamento(self):
        pass

    def diagonalizacao(self):
        v = list()
        aux = list()
        aux2 = list()
        for j in range(0, self.get_m()):
            aux2.clear()
            for k in range(0, self.get_n()):
                v.append(self.__mat[j][k]/self.__mat[j][j])
            self.__mat[j] = v.copy()
            pivo = j
            for k in range(j, self.get_m()):
                print(self.__mat[k][j])
                if fabs(self.__mat[k][j]) < fabs(self.__mat[pivo][j]):
                    pivo = k
            aux2 = self.__mat[j].copy()
            self.__mat[j] = self.__mat[pivo].copy()
            self.__mat[pivo] = aux2.copy()
            for i in range(0, self.get_m()):
                aux.clear()
                if i != j:
                    for k in range(0, self.get_n()):
                        aux.append(self.__mat[j][k] * self.__mat[i][j])
                    self.__mat[j] = aux.copy()
                    for k in range(0, self.get_n()):
                        self.__mat[i][k] = self.__mat[i][k] - self.__mat[j][k]
                    self.__mat[j] = v.copy()
            v.clear()
        self.__escrita_arquivos()


def criacao_arquivos():
    entrada = open('Entrada2.txt', 'x')
    saida = open('Saida.txt', 'x')
    entrada.close()
    saida.close()
