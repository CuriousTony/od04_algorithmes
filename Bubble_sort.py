import random


def bubble_sort(data):
    for step in range(len(data)):
        for index in range(len(data) - step - 1):
            if data[index] > data[index + 1]:
                data[index], data[index+1] = data[index+1], data[index]

    return data


data_list = [n for n in range(1, 41)]
random.shuffle(data_list)
print(f'Исходный список:\n {data_list}')
print(f'Отсортированный список:\n {bubble_sort(data_list)}')
