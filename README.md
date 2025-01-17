# od04_algorithmes
В данной работе произведены имзмерения зависимости расхода времени и памати от размеров обрабатываемых массивов данных.
#### Основные выводы:
### Алгоритм: Бинарный поиск.
Сложность: O(log n).

Обоснование:
Бинарный поиск работает на отсортированном массиве.
На каждом шаге алгоритм делит массив на две части и сравнивает искомый элемент с элементом в середине массива.
Если искомый элемент меньше среднего, поиск продолжается в левой половине массива.
Если искомый элемент больше среднего, поиск продолжается в правой половине массива.
Процесс повторяется, пока элемент не будет найден или пока массив не закончится.

Анализ сложности:
На каждой итерации размер массива уменьшается в 2 раза.
Количество итераций, необходимых для нахождения элемента, равно количеству раз, которое можно разделить массив пополам, пока не останется один элемент.
Это выражается как log₂(n).

В Big O нотации основание логарифма опускается, поэтому сложность бинарного поиска — O(log n).

Пример:
Для массива из 16 элементов потребуется не более 4 итераций (log₂16 = 4).
Для массива из 1024 элементов потребуется не более 10 итераций (log₂1024 = 10).

Заключение:
Бинарный поиск является эффективным алгоритмом для поиска элемента в отсортированном массиве. Его временная сложность O(log n) делает его значительно быстрее линейного поиска (O(n)) для больших массивов.


### Алгоритм: Пузырьковая сортировка.
Сложность: O(n²).

Обоснование:
Пузырьковая сортировка проходит по массиву несколько раз, сравнивая соседние элементы и меняя их местами, если они стоят в неправильном порядке.
После каждого прохода самый большой элемент "всплывает" в конец массива.
Процесс повторяется, пока весь массив не будет отсортирован.

Анализ сложности:
Внешний цикл выполняется n раз, где n — количество элементов в массиве.
Внутренний цикл на каждом шаге внешнего цикла выполняется n - i - 1 раз, где i — текущий шаг внешнего цикла.

Пример:
Для массива из 10 элементов потребуется до 45 сравнений и обменов.
Для массива из 100 элементов потребуется до 4950 сравнений и обменов.

Заключение:
Пузырьковая сортировка является простым, но неэффективным алгоритмом для сортировки больших массивов. Её временная сложность O(n²) делает её непригодной для работы с большими объемами данных, но она может быть полезна для обучения и понимания основ сортировки.
