def sum_negatives_between_max_min(arr):
    if not arr:
        return 0

    # Находим индексы первого максимума и первого минимума
    idx_max = arr.index(max(arr))
    idx_min = arr.index(min(arr))

    # Определяем границы диапазона (от меньшего индекса к большему)
    left = min(idx_max, idx_min)
    right = max(idx_max, idx_min)

    # Суммируем отрицательные элементы строго между границами
    total = 0
    for i in range(left + 1, right):
        if arr[i] < 0:
            total += arr[i]

    return total


if __name__ == "__main__":
    # Пример 1
    A = [3, -5, 2, -8, 7, -1, 4]
    print("Массив:", A)
    print("Максимум:", max(A), "| Минимум:", min(A))
    print("Сумма отрицательных между ними:", sum_negatives_between_max_min(A))

    # Пример 2 (минимум раньше максимума)
    B = [-10, 2, -3, 5, 1, -7, 12]
    print("\nМассив:", B)
    print("Максимум:", max(B), "| Минимум:", min(B))
    print("Сумма отрицательных между ними:", sum_negatives_between_max_min(B))