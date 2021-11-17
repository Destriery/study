
def reduce_sequence(string: str) -> str:
    """Посчитать дублирующиеся подряд символы
        '' -> ''
        'AABBDD' -> 'A2B2D2'
        'ABC' -> 'ABC'
        'A' -> 'A'
        'AABCCD' -> 'A2BC2D'
        'ABA' -> 'ABA'
    """

    result = ''
    current = ''
    num = 0

    for char in string:
        if char != current:
            result = result + current + (str(num) if num > 1 else '')
            current = char
            num = 1
        else:
            num += 1

    return result + current + (str(num) if num > 1 else '')


def reduce_sequence2(string: str) -> str:
    result = ''
    current = ''
    num = 1

    for char in string + ' ':
        if char != current:
            result = result + current + (str(num) if num > 1 else '')
            current = char
            num = 1
        else:
            num += 1

    return result


# tests
def tests():
    cases = {
        '': '',
        'AABBDD': 'A2B2D2',
        'ABC': 'ABC',
        'A': 'A',
        'AABCCD': 'A2BC2D',
        'ABA': 'ABA'
    }

    for case, result in cases.items():
        assert reduce_sequence(case) == result,\
            f'The result of {case} should be {result}, not be {reduce_sequence(case)}'

        assert reduce_sequence2(case) == result,\
            f'The result of {case} should be {result}, not be {reduce_sequence2(case)}'


if __name__ == '__main__':
    tests()
