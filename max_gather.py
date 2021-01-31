def get_max_apples(A: list, K: int, L: int):
    if K < 0 or L < 0 or ((K + L) > len(A)):
        return -1
    bigger = K if K > L else L
    smaller = L if K > L else K

    first = max_interval(A, bigger, smaller)    # tupla com soma das maçãs e índice inicial de coleta
    remain_left = A[:first[1]]                  # lista com as árvores à esquerda do limite do primeiro coletor
    remain_right = A[(first[1]+bigger):]        # lista com as árvores à direita

    second_left = max_interval(remain_left, smaller, 0)
    second_right = max_interval(remain_right, smaller, 0)
    second = [0, 0]
    if second_left[0] > second_right[0]:
        second = list(second_left)
    else:
        second = list(second_right)
        # indice inicial do segundo intervalo + indice inicial do primeiro + comprimento do primeiro
        second[1] = second[1] + first[1] + bigger

    max_apples = first[0]+second[0]
    k_index = first[1] if K > L else second[1]
    l_index = second[1] if K > L else first[1]

    return max_apples, k_index, l_index


def max_interval(arr, qty, remain_qty):
    start_index = 0
    max_sum = 0
    curr_sum = 0

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
        if curr_sum > max_sum and True:
            max_sum = curr_sum
            start_index = i

    return max_sum, start_index
