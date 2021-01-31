def get_max_apples(A: list, K: int, L: int):
    """
    Calcula o número máximo de itens que podem ser coletadas por dois coletores em um intervalo
    :param A: lista de inteiros positivos
    :param K: inteiro positivo
    :param L: inteiro positivo
    """
    # Trata parâmetros recebidos
    try:
        K = int(K)
        L = int(L)
        if type(A) == str:
            A = list(A.strip("[]{}()").split(","))

        for i in range(0, len(A)):
            A[i] = int(A[i])
    except:
        raise ValueError('Valores informados não permitem calcular a coleta')
        print("Parâmetros inválidos")
        return -1, 0, 0

    if K < 0 or L < 0 or ((K + L) > len(A)):
        resp = -1, 0, 0
        return resp

    def calculate_max(first, second):
        # tupla com soma das maçãs e índice inicial de coleta
        first_gatherer = max_interval(A, first, second)

        # lista com as árvores à esquerda do limite do primeiro coletor
        remain_left = A[:first_gatherer[1]]

        # lista com as árvores à direita
        remain_right = A[(first_gatherer[1] + first):]

        gather_left = max_interval(remain_left, second, 0)
        gather_right = max_interval(remain_right, second, 0)
        second_gatherer = [0, 0]
        if gather_left[0] > gather_right[0]:
            second_gatherer = list(gather_left)
        else:
            second_gatherer = list(gather_right)
            # indice inicial do segundo intervalo + indice inicial do primeiro + comprimento do primeiro
            second_gatherer[1] = second_gatherer[1] + first_gatherer[1] + first

        max_apples = first_gatherer[0] + second_gatherer[0]
        result = max_apples, first_gatherer[1], second_gatherer[1]
        return result

    starting_left = calculate_max(K, L)
    starting_right = calculate_max(L, K)
    resp = []
    if starting_left[0] >= starting_right[0]:
        resp = starting_left
    else:
        resp = starting_right[0], starting_right[2], starting_right[1]

    return resp


def max_interval(arr, qty, remain_qty):
    """
    Calcula o número máximo de itens num dado intervalo, considerando árvores restantes para o próximo coletor
    :param arr: lista de inteiros
    :param qty: inteiro positivo
    :param remain_qty: inteiro positivo
    """
    start_index, max_sum, curr_sum = 0, 0, 0

    for i in range(0, len(arr)):
        if (i + qty) > len(arr):
            break
        # Se não houver itens à esquerda nem à direita suficientes para o restante, pula iteração
        over_left = (i - remain_qty) < 0
        over_right = (i + qty + remain_qty) > len(arr)
        if over_left and over_right:
            continue
        curr_sum = 0
        for j in range(i, qty+i):
            curr_sum += arr[j]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start_index = i

    return max_sum, start_index
