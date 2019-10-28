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

    def __pivotamento(self, j):
        pass

    def __diagonalizacao(self):
        pass


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

    def __convergenciaLinhas(self):
        pass

    def __convergenciaSassenfeld(self):
        pass

    def __sistemaIterativo(self):
        pass


class SistemaEquacoes(GaussJordan, GaussSeidel):
    def __init__(self, dim):
        self.__mat = list()
        self.__dimencao = dim
        self.__leitura_arquivos()
        self.set_m(len(self.get_mat()))
        self.set_n(self.get_m() + 1)
        self.set_k(500)
        self.set_e(0.0000000001)
        self.__diagonalizacao()
        self.__sistemaIterativo()

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
                mat_aux[i][j] = float(mat_aux[i][j])
        self.set_mat(mat_aux)

    def __escrita_arquivos(self):
        saida = open('Saida.txt', 'w')
        saida.write(f'Sistema de dimencao {self.get_m()}:\nMatriz diagonalizada: {self.get_mat()} \n')
        for i in range(self.get_m()):
            saida.write(str(self.__mat[i][-1]) + ' ')
        saida.write('\n')

    # resolusão gauss-jordan
    def __pivotamento(self):
        matriz = self.get_mat().copy()
        ntrocas = 0
        for k in range(0, self.get_m() - 1):
            maximo = fabs(matriz[k][k])
            pivo = k
            # procurar o maior da coluna onde esta o pivot
            for i in range(k + 1, self.get_m()):
                if fabs(matriz[i][k]) > maximo:
                    maximo = fabs(matriz[i][k])
                    pivo = i
            # se o maior nao e o pivot...
            if pivo != k:
                # troca a linha onde esta o pivot actual pela linha onde esta o novo pivot
                ntrocas += 1
                for j in range(0, self.get_n()):
                    aux = matriz[k][j]
                    matriz[k][j] = matriz[pivo][j]
                    matriz[pivo][j] = aux

        self.set_mat(matriz.copy())

    def __diagonalizacao(self):
        matri_aux = self.get_mat().copy()
        v = list()
        aux = list()
        aux2 = list()
        erro = False
        for j in range(0, self.get_m()):
            aux2.clear()
            for k in range(0, self.get_n()):
                try:
                    v.append(self.__mat[j][k] / self.__mat[j][j])
                except ZeroDivisionError:
                    mat = self.__mat.copy()
                    erro = True
                self.__pivotamento()
            self.__mat[j] = v.copy()
            for i in range(0, self.get_m()):
                aux.clear()
                if i != j:
                    if erro:
                        break
                    for k in range(0, self.get_n()):
                        aux.append(self.__mat[j][k] * self.__mat[i][j])
                    self.__mat[j] = aux.copy()
                    for k in range(0, self.get_n()):
                        self.__mat[i][k] = self.__mat[i][k] - self.__mat[j][k]
                    self.__mat[j] = v.copy()
            v.clear()
        arq = open('Saida.txt', 'a')
        print(f'Sistema de dimencao {self.get_m()}:\nMatriz diagonalizada: {self.get_mat()}')
        arq.write('\n')
        if erro:
            if mat[- 1][-1] == mat[-1][-2]:
                print("SPI")
            else:
                print("SI")
        else:
            self.__escrita_arquivos()
            # arq.write(f'Matriz diagonalizada: {self.get_mat()}')
        arq.close()
        self.set_mat(matri_aux.copy())

    # resolução iterativa
    def __convergenciaLinhas(self):
        conv = list()
        for i in range(0, len(self.__mat)):
            sum_aij = 0
            for j in range(0, self.get_m()):
                if j != i:
                    sum_aij += fabs(self.__mat[i][j])
            ajj = fabs(self.__mat[i][i])
            # print(f"Conve: {sum_aij / ajj}")
            if sum_aij < ajj:
                conv.append(True)
            else:
                conv.append(False)
        arq = open('Saida.txt', 'a')
        print('Convergencia de linhas: ', end='')
        if False not in conv:
            print("Converge")
        else:
            print("Não é possivel garantir a convergencia")
        arq.close()

    def __convergenciaSassenfeld(self):
        l2 = list()
        conv = list()
        cont = aux = sum_aij = 0
        for i in range(1, 3):
            sum_aij += fabs(self.__mat[0][i])
        l2.append(sum_aij / fabs(self.__mat[0][0]))
        for i in range(1, self.get_m()):
            cont = aux = 0
            for j in range(0, self.get_m()):
                if j != i:
                    if cont < len(l2):
                        aux += fabs(self.__mat[i][j]) * l2[cont]
                    else:
                        aux += fabs(self.__mat[i][j])
                cont += 1
            try:
                l2.append(fabs(aux) / fabs(self.__mat[i][i]))
            except ZeroDivisionError:
                break

            if l2[-1] < 1:
                conv.append(True)
            else:
                conv.append(False)
        arq = open('Saida.txt', 'w')

        print('Convergencia de Sassenfeld: ', end='')
        if False not in conv:
            print("Converge")
        else:
            print("Não é possivel garantir a convergencia")
        arq.close()

    def __sistemaIterativo(self):
        self.__pivotamento()
        self.__convergenciaSassenfeld()
        self.__convergenciaLinhas()
        y = list()
        x = list()
        k = 0
        mat_aux = list()
        mat_aux.append(self.__mat.copy())
        self.__pivotamento()
        for i in range(0, self.get_m()):
            y.append(0.0)
            x.append(1.0)
        while True:
            numerado = 0
            denominador = 1
            for i in range(0, self.get_m()):
                y[i] = 0  # yi e o xi ele k + 1
                for j in range(0, self.get_m()):
                    if j != i:
                        y[i] += self.__mat[i][j] * x[j]
                try:
                    y[i] = (self.__mat[i][-1] - y[i]) / self.__mat[i][i]
                    yi = y[i]
                    xi = x[i]
                except ZeroDivisionError:
                    print(end='')
                if denominador < fabs(yi):
                    denominador = fabs(yi)
                if numerado < fabs(yi) - fabs(xi):  # guarda o maximo da diferença de xek e xek-1
                    numerado = fabs(yi - xi)
                x[i] = y[i]
                erro = numerado / denominador

            if erro < self.get_e() and k >= self.get_k():
                break
            k += 1
        arq = open('Saida.txt', 'w')
        print(f'Vetor resposta do metodo iterativo: {x}\n')
        print('\033[1;94m-=\033[m' * 70, '\n')
        arq.close()


def valor_max(x):
    mx = max(x)
    mi = min(x)
    if fabs(mx) >= fabs(mi):
        return fabs(mx)
    else:
        return fabs(mi)


def criacao_arquivos():
    entrada = open('Entrada2.txt', 'x')
    saida = open('Saida.txt', 'x')
    entrada.close()
    saida.close()
