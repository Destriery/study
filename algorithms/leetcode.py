from collections import defaultdict


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
        if item in current and current[item] >= start:
            result = max((result, (i - start)))
            start = current[item] + 1

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


def get_valid_sum(array: list, _max: int, count: int) -> int | None:
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


class Palindrome:
    @classmethod
    def isPalindrome(cls, s: str) -> bool:
        for index in range(len(s) // 2):
            if s[index] != s[-index - 1]:
                return False

        return True

    @classmethod
    def longestPalindrome(cls, s: str) -> str:
        reversed_s = ''.join(reversed(s))

        for _num in range(len(s), 0, -1):
            for start in range(len(s) - (_num - 1)):
                substr = s[start:start + _num]
                reverse_substr = reversed_s[-(start + _num):-start] if start else reversed_s[-(start + _num):]

                if substr == reverse_substr:
                    return substr

        return ''


class Zigzag:
    @classmethod
    def convert(cls, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1: return s

        strings = [[] for _ in range(numRows)]

        substr_list = (
            s[start * (numRows * 2 - 2): start * (numRows * 2 - 2) + (numRows * 2 - 2) + 1]
            for start in range(len(s) // numRows)
        )
        if len(s) <= numRows: substr_list = [s]

        for substr in substr_list:
            for i in range(numRows):
                if len(substr) == i: break
                strings[i].append(substr[i])

            for i, char in enumerate(substr[numRows:]):
                str_index = numRows - (i % numRows) - 2

                strings[str_index].append(char)

        result = []
        for _ in strings:
            result += _

        print(strings)

        return ''.join(result)


'''
P   A   H   N
A P L S I I G
Y   I   R
'''


class RomanToInt:
    mapping = {
        'I': (0, 1),
        'V': (1, 5),
        'X': (2, 10),
        'L': (3, 50),
        'C': (4, 100),
        'D': (5, 500),
        'M': (6, 1000)
    }

    def romanToInt(self, s: str) -> int:
        """
        1. Go from right to left
        2. Know about the previos roman digit
        3. If the current one matches the previous one or follows it in the mapping,
            add it to the result and change the previous one to the current one
        4. If the previous one follows the current one in the mapping,
            subtract it
        """
        result = 0
        previous_roman = 'I'
        index = len(s) - 1

        while index >= 0:
            roman = s[index]

            if self.mapping[roman][0] >= self.mapping[previous_roman][0]:
                result += self.mapping[roman][1]
                previous_roman = roman
            else:
                result -= self.mapping[roman][1]

            index -= 1

        return result


class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        current_prefix = strs[0]

        for string in strs:
            for i in range(min(len(current_prefix), len(string))):
                if current_prefix[i] != string[i]:
                    current_prefix = current_prefix[:i]
                    break

            if current_prefix == '':
                return current_prefix

        return current_prefix


class ThreeSum:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
            либо:
                - [0, 0, 0]
                - [-x, 0, x]
                - [-(x + y), x, y]
        """
        results = []

        minus_dict = {}
        minus_list = []
        zero_list = []
        plus_list = []

        # подготавливаем списки и словарь
        for num in nums:
            if num == 0:
                zero_list.append(0)
            elif num < 0:
                minus_list.append(num)
                minus_dict[-num] = [num, 0, -num]
            else:
                plus_list.append(num)

        # находим [0, 0, 0]
        if len(zero_list) >= 3:
            results.append([0, 0, 0])

        # находим [-x, 0, x]
        if len(zero_list) > 0:
            for num in plus_list:
                if num in minus_dict:
                    results.append(minus_dict[num])

        # находим [-(x + y), x, y]
        minus_dict = defaultdict(list)
        for i in range(len(minus_list)):
            for j in range(i + 1, len(minus_list)):
                third = 0 - (minus_list[i] + minus_list[j])
                if not [minus_list[i], minus_list[j], third] in minus_dict[third]:
                    minus_dict[third].append([minus_list[i], minus_list[j], third])

        plus_dict = defaultdict(list)
        for i in range(len(plus_list)):
            for j in range(i + 1, len(plus_list)):
                third = 0 - (plus_list[i] + plus_list[j])
                if not [plus_list[i], plus_list[j], third] in plus_dict[third]:
                    plus_dict[third].append([plus_list[i], plus_list[j], third])

        for num in plus_list:
            results.extend(minus_dict[num])

        for num in minus_list:
            results.extend(plus_dict[num])

        return results


def removeDuplicates(nums: list[int]) -> int:
    unique_index = 0
    current_num = nums[0]
    current_index = 0

    while current_index < len(nums):
        if nums[current_index] != current_num:
            nums[unique_index] = current_num
            current_num = nums[current_index]
            unique_index += 1

        current_index += 1

    return unique_index if current_num != nums[-1] else unique_index + 1


def searchInsert(nums: list[int], target: int) -> int | None:
    while len(nums) > 0:
        center_index = len(nums) // 2

        if nums[center_index] == target:
            return center_index
        elif target < nums[center_index]:
            if len(nums) == 1:
                return center_index
            nums = nums[:center_index]
        elif target > nums[center_index]:
            if len(nums) == 1:
                return center_index + 1
            nums = nums[center_index:]


def years(_input: str):
    MAX_LEN = 10

    inp = _input.strip()
    i = len(inp) - 1

    s = [0] * MAX_LEN

    for index, j in enumerate(reversed(inp)):
        s[index] = int(j)

    cur_set = set()
    while True:
        if i + 1 == MAX_LEN:
            print(str(-1))
            break

        if s[i] in (0, 2) or s[i] in cur_set:
            if s[i] == 10 or s[i] + 1 == 10:
                s[i] = 3
                if i + 1 == MAX_LEN:
                    print(str(-1))
                    break

                cur_set.remove(s[i + 1])
                s[i + 1] += 1
                if s[i + 1] == 10:
                    i += 2
                else:
                    i += 1
            else:
                s[i] += 1

            for _ in range(i):
                s[_] = 1
        else:
            cur_set.add(s[i])
            i -= 1

            if i < 0:
                print(''.join(str(i) for i in reversed(s) if i > 0))
                break
