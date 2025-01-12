import time
import random
from memory_profiler import memory_usage
import matplotlib.pyplot as plt


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


# Функция для измерения времени и памяти
def measure_performance(search_function, data, target):
    start_time = time.time()
    search_function(data, target)  # Выполняем поиск
    end_time = time.time()
    execution_time = end_time - start_time

    # Измеряем использование памяти
    mem_usage = memory_usage((search_function, (data, target)), max_usage=True)

    return execution_time, mem_usage


if __name__ == '__main__':
    list_sizes = [10, 100, 1000, 10000, 100000, 1000000]
    times = []
    memories = []

    # Запуск тестов
    for size in list_sizes:
        data = [n for n in range(size)]
        target = random.choice(data)  # Выбираем случайный элемент для поиска

        time_taken, mem_used = measure_performance(binary_search, data, target)
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
    plt.xscale('log')  # Логарифмическая шкала для оси X
    plt.grid(True)

    # График использования памяти
    plt.subplot(1, 2, 2)
    plt.plot(list_sizes, memories, marker='o', linestyle='-', color='r')
    plt.title('Зависимость использования памяти от размера списка')
    plt.xlabel('Размер списка')
    plt.ylabel('Память (MiB)')
    plt.xscale('log')  # Логарифмическая шкала для оси X
    plt.grid(True)

    plt.tight_layout()
    plt.show()
