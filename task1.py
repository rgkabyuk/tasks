# если повторяющиеся элементы не нужны
# сложность O(n+m), n = len(list_1), m = len(list_2)

print(set(list_1).difference(list_2))
