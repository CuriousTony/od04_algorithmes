import time
import random
from memory_profiler import memory_usage
import matplotlib.pyplot as plt


def bubble_sort(data):
    for step in range(len(data)):
        for index in range(len(data) - step - 1):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
    return data


# Функция для измерения времени и памяти
def measure_performance(sort_function, data):
    start_time = time.time()
    sort_function(data.copy())  # Используем копию, чтобы не изменять исходный список
    end_time = time.time()
    execution_time = end_time - start_time

    # Измеряем использование памяти
    mem_usage = memory_usage((sort_function, (data.copy(),)), max_usage=True)

    return execution_time, mem_usage


if __name__ == '__main__':
    list_sizes = [10, 100, 500, 1000, 2000, 5000]
    times = []
    memories = []

    # Запуск тестов
    for size in list_sizes:
        data = [n for n in range(size)]
        random.shuffle(data)

        time_taken, mem_used = measure_performance(bubble_sort, data)
        times.append(time_taken)
        memories.append(mem_used)

        print(f"Размер списка: {size}, Время: {time_taken:.6f} сек, Память: {mem_used} MiB")

    # Построение графиков
    plt.figure(figsize=(12, 6))

    # График времени выполнения
    plt.subplot(1, 2, 1)
    plt.plot(list_sizes, times, marker='o', linestyle='-', color='b')
    plt.title('Зависимость времени выполнения от размера списка')
    plt.xlabel('Размер списка')
    plt.ylabel('Время (сек)')
    plt.grid(True)

    # График использования памяти
    plt.subplot(1, 2, 2)
    plt.plot(list_sizes, memories, marker='o', linestyle='-', color='r')
    plt.title('Зависимость использования памяти от размера списка')
    plt.xlabel('Размер списка')
    plt.ylabel('Память (MiB)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
