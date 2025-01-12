def binary_search(data, target):
    start, end = 0, len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


rand_list = [n for n in range(1, 21)]
print(rand_list)  # для наглядности вывода
print(binary_search(rand_list, 16))
