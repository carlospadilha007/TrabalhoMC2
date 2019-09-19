def criacao_arquivos():
    entrada = open('Entrada2.txt', 'x')
    saida = open('Saida.txt', 'x')
    entrada.close()
    saida.close()


def leitura_arquivos(var):
    entrada = open(f'Entrada{var}.txt', 'r')
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
    return mat_aux


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
mat = leitura_arquivos(2)
print(mat)
