def get_max_apples(A, K, L):
    """
    Calcula o número máximo de itens que podem ser coletadas por dois coletores em um intervalo

    :param A: lista de inteiros positivos
    :param K: inteiro positivo
    :param L: inteiro positivo
    """
    resp = -1, 0, 0

    # Trata parâmetros recebidos
    try:
        K = int(K)
        L = int(L)
        if type(A) == str:
            A = list(A.strip("[]{}()").split(","))

        for i in range(0, len(A)):
            A[i] = int(float(A[i]))
    except:
        raise ValueError('Valores informados não permitem calcular a coleta')
        # return -1, 0, 0

    if K < 0 or L < 0 or ((K + L) > len(A)):
        return resp

    def iterate_sum():
        max_sum, k_index, l_index = 0, 0, 0
        last_valid_i = len(A) - K - L + 1
        last_valid_j = len(A) - L + 1

        # Percorre array verificando continuamente se soma total é a máxima possível
        for i in range(0, last_valid_i):
            k_sum = 0

            # Soma valores do intervalo K iniciado em i
            for ik in range(i, i + K):
                k_sum += A[ik]

            # Para cada item a partir do fim do intervalo K, itera para obter a maior soma possível do intervalo L
            for j in range(i + K, last_valid_j):
                curr_sum, l_sum = 0, 0

                # Soma valores do intervalo L iniciado em j
                for jl in range(j, j + L):
                    l_sum += A[jl]

                curr_sum = k_sum + l_sum
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    k_index = i
                    l_index = j

        return max_sum, k_index, l_index

    # Repete cálculo invertendo a ordem dos coletores (somente se tamanhos dos intervalos K e L forem diferentes)
    resp = iterate_sum()
    if K != L:
        K, L = L, K
        reverse_i = iterate_sum()
        if reverse_i[0] > resp[0]:
            resp = reverse_i[0], reverse_i[2], reverse_i[1]

    return resp
