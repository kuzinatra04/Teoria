from itertools import permutations


def binary_permutations(s1, s2):
    # Генерируем все возможные перестановки для s1
    perms = [''.join(p) for p in permutations(list(s1))]

    count = 0
    for perm in perms:
        # Проверяем, можно ли получить s2 из текущей перестановки
        if s2 in perm:
            count += 1

    return count


# Пример использования
s1 = "203122010"
s2 = "032012012"
result = binary_permutations(s1, s2)
print("Количество перестановок:", result)
