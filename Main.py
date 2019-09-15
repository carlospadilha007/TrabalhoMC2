def criacao_arquivos():
    entrada = open('Entrada.txt', 'x')
    saida = open('Saida.txt', 'x')
    entrada.close()
    saida.close()


def leitura_arquivos():
    entrada = open('Entrada.txt', 'r')
    linhas = ''
    l = list()
    mat = list()
    linhas = entrada.readlines()
    for i in range(0, len(linhas)):
        l = linhas[i].strip().split(',')
        mat.append(l.copy())
    return mat


def escrita_arquivos(mat):
    saida = open('Saida.txt', 'w')
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if j < len(mat[i]) - 1:
                saida.write(mat[i][j] + ', ')
            else:
                saida.write(mat[i][j])
        saida.write('\n')


# Main
mat = leitura_arquivos()
escrita_arquivos(mat)
