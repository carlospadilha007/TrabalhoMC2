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
        self.__e = int()

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
        self.leitura_arquivos()

    def get_mat(self):
        return self.__mat

    def get_dimencao(self):
        return self.__dimencao

    def set_mat(self, mat):
        self.__mat = mat

    def set_dimencao(self, dimecao):
        self.__dimencao = dimecao

    def leitura_arquivos(self):
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
        self.set_mat(mat_aux)

    def escrita_arquivos(self):
        saida = open('Saida.txt', 'w')
        for i in range(len(self.__mat)):
            for j in range(len(self.__mat[i])):
                if j < len(self.__mat[i]) - 1:
                    saida.write(self.__mat[i][j] + ', ')
                else:
                    saida.write(self.__mat[i][j])
            saida.write('\n')


def criacao_arquivos():
    entrada = open('Entrada2.txt', 'x')
    saida = open('Saida.txt', 'x')
    entrada.close()
    saida.close()
