"""Нахождение наибольшей подстроки с неповторяющимися элементами.
    Примеры:
        Input: s = "abcabcbb"
        Output: 3

        Input: s = "bbbbb"
        Output: 1

        Input: s = "pwwkew"
        Output: 3

"""


def lengthOfLongestSubstring_v1(s: str) -> int:
    """Вариант через список. Используем временный список для сохранения текущего варианта последовательности.

        1. Перебираем строку посимвольно, сохраняя каждый во временный список current
        2. На каждом шаге проверяем вхождение следующего элемента в current
        3. Если находим, записываем max((result, len(current))) в результат.
        4. current создаем заново, начиная с элемента, слудующего за повторенным.
    """
    result = 0
    current = []
    for item in s:
        if item in current:
            result = max((result, len(current)))
            index = current.index(item)
            current = current[index + 1:] if index + 1 < len(current) else []

        current.append(item)

    result = max((result, len(current)))

    return result


def lengthOfLongestSubstring_v2(s: str) -> int:
    """Вариант через словарь. Быстрее предыдущего так как ищем совпадения в словаре и не пересоздаем список
        1. Перебираем строку посимвольно, сохраняя каждый во временный словарь current
        2. На каждом шаге проверяем вхождение следующего элемента в current
        3. Так как в отличие от предыдущего варианта словарь мы не пересоздаем,
            нам нужно понимать с какой позиции вести отчет. Для этого используем переменную start.
            Соответственно проверяем совпадающий элемент в текущей последовательности до или после start
        4. Если элемент внутри последовательности, то есть больше или равен start ->
            увеличиваем start на 1 и записываем новый результат max((result, (i - start)))
    """
    result = 0
    current = {}
    start = 0

    for i, item in enumerate(s):
        if item in current and current.get(item) >= start:
            result = max((result, (i - start)))
            start = current.get(item) + 1

        current[item] = i

    result = max((result, (len(s) - start)))

    return result


def reverse(self, x: int) -> int:
    """Получить число с цифрами в обратном порядке
        x = 12345
        return 54321

        Если x < -2 ** 31 или x > 2 ** 31 - 1 вернуть 0
    """
    if x < 0:
        x *= -1
        _max = 2 ** 31
        result = 0
        for i in range(len(str(x))):
            result = result * 10 + x % 10
            x = x // 10

        if result <= _max:
            return result * -1

        else:
            return 0

    elif x > 0:
        _max = 2 ** 31
        result = 0
        for i in range(len(str(x))):
            result = result * 10 + x % 10
            x = x // 10

        if result < _max:
            return result

        else:
            return 0

    else:
        return 0


def get_valid_sum(array: list, _max: int, count: int) -> int:
    """Есть массив целых чисел например [50, 57, 53, 56, 58, 51, 81] есть переменная max и переменная count:
        Max отвечает за число превышать которое нельзя
        Count - отвечает за то, сколько чисел из массива мы должны сложить.
        В функцию передаются все эти аргументы, далее складывая count чисел в массиве,
        мы должны вернуть сумму максимально близкую к max
        Например если мы передаём в функцию
        (163, 3, [50, 57, 53, 56, 58, 51, 81])
        То вернуться должно 163 т.к. числа 50+57+56 в сумме дадут 163 а это и есть наш max

        import itertools
        def choose_best_sum(t, k, ls):
            '''Лучшее решение задачи с codewars =)'''
            try:
                return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
            except:
                return None
    """
    result_max = 0
    tree = {'list': array, 'sum': 0}
    current_line = [tree]
    for step in range(count):
        new_line = []
        for item in current_line:
            for i, num in enumerate(item['list']):
                item[num] = {
                    'list': item['list'][i + 1:],
                    'sum': item['sum'] + num,
                    # 'expr': f"{item['expr']} + {num}" if item.get('expr') else str(num)
                }

                new_line.append(item[num])

                if step == count - 1 and item[num]['sum'] <= _max:
                    result_max = max([result_max, item[num]['sum']])

        current_line = new_line

    return result_max if result_max else None
