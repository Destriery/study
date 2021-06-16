

def bubble(array: list) -> list:
    """Пузырьковая сортировка O(n**2)

        1. Сравниваем первые два элемента.
        2. Меням их (или нет) так, чтобы меньший шел первым.
        3. Сдвигаемся дальше на один элемент и повторяем сравнение.
        4. Доходим до конца и начинаем сначала.
        5. Если в проходке нет изменений, завершаем алгоритм.

        * последний элемент в каждом проходе считается отсортированным, так что второй раз по нему(и далее) не идем
    """

    length = len(array)

    # в случае использования is_changed время выполнения увеличится
    for j in range(length - 1):
        # is_changed = False
        for i in range(length - j - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                # is_changed = True

        # if not is_changed:
        #     break

    return array


def bubble_from_inet(array):
    """https://younglinux.info/algorithm/bubble"""
    N = len(array)

    for i in range(N - 1):
        for j in range(N - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff

    return array


def shaker(array: list) -> list:
    """Шейкерная сортировка O(n**2) - чуть лучше пузырьковой

        1. Сравниваем первые два элемента.
        2. Меням их (или нет) так, чтобы меньший шел первым.
        3. Сдвигаемся дальше на один элемент и повторяем сравнение.
        4. Доходим до конца и начинаем двигаться в обратном порядке аналогично сравнивая элементы.
        5. Доходим до начала и опять меняем направления движения.
        6. Если в проходке нет изменений, завершаем алгоритм.

        * конечные элементы в проходе считаются отсортированными, так что второй раз по ним не идем
    """
    length = len(array)

    for j in range(length - 1):
        is_changed = False

        for i in range(j, length - j - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_changed = True

        for i in range(length - j - 2, j - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_changed = True

        if not is_changed:
            break

    return array


def cocktail_shaker_sort_from_inet(unsorted: list) -> list:
    """https://github.com/TheAlgorithms/Python/blob/master/sorts/cocktail_shaker_sort.py"""
    for i in range(len(unsorted) - 1, 0, -1):
        swapped = False

        for j in range(i, 0, -1):
            if unsorted[j] < unsorted[j - 1]:
                unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
                swapped = True

        for j in range(i):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                swapped = True

        if not swapped:
            break
    return unsorted


def odd_even(array: list) -> list:
    """Четно-нечетная сортировка O(n**2) - в худшем случае. Но в среднем O(n*log(n)), а в лучшем даже O(n)

        1. Сравниваем первые два элемента.
        2. Меням их (или нет) так, чтобы меньший шел первым.
        3. Сдвигаемся на 2 позиции вправо (идем по нечетным элементам) и посторяем сравнение.
        4. Дойдя до конца, начинаем новый проход со второго элемента

        * в отличие от предыдущих сортировок,
            конец алгоритма может быть только при четной и нечетной проходке без изменений,
            так как тут мы не сдвигаем самый большой элемент сразу вправо, а двигаем сразу несколько,
            но когда они дойдут до конца - заранее не известно.
    """

    length = len(array)
    is_changed = True

    while is_changed:
        is_changed = False

        for i in range(0, length - 1, 2):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_changed = True

        for i in range(1, length - 1, 2):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_changed = True

    return array


def odd_even_sort_from_inet(input_list: list) -> list:
    """https://github.com/TheAlgorithms/Python/blob/master/sorts/odd_even_sort.py"""
    sorted = False
    while sorted is False:  # Until all the indices are traversed keep looping
        sorted = True
        for i in range(0, len(input_list) - 1, 2):  # iterating over all even indices
            if input_list[i] > input_list[i + 1]:

                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                # swapping if elements not in order
                sorted = False

        for i in range(1, len(input_list) - 1, 2):  # iterating over all odd indices
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                # swapping if elements not in order
                sorted = False
    return input_list
