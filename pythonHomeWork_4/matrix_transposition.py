# Задача:
# Напишите функцию для транспонирования матрицы

source_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 2, 1]]


def matrix_transposition(matrix: list) -> list:
    """
    Функция для транспонирования матрицы

    :param matrix: исходная матрица
    :return: result - транспонированная матрица
    """
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result


print('Исходная матрица:')
print(*source_matrix, sep='\n')

result_matrix = matrix_transposition(source_matrix)
print('\nТранспонированная матрица:')
print(*result_matrix, sep='\n')
