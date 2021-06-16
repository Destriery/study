import json
import random

from utils.profilers import Profiler

from .sorts import bubble, bubble_from_inet, shaker, cocktail_shaker_sort_from_inet, odd_even, odd_even_sort_from_inet

max = 1000

arrays = (
    [i for i in range(max)],
    sorted([i for i in range(max)], key=lambda x: random.random()),
    [i for i in reversed(range(max))],
)
_result = [i for i in range(max)]


profiler = Profiler()


def sort_test(func):
    print('\n')
    current_arrays = json.loads(json.dumps(arrays))

    for i, array in enumerate(current_arrays):
        profiler.start()
        func(array)
        profiler.stop()

        print(f'{i}: {profiler.result_time}')

        assert array == _result


def test__bubble():
    sort_test(bubble)


def test__bubble_from_inet():
    sort_test(bubble_from_inet)


def test__shaker():
    sort_test(shaker)


def test__cocktail_shaker_sort_from_inet():
    sort_test(cocktail_shaker_sort_from_inet)


def test__odd_even():
    sort_test(odd_even)


def test__odd_even_sort_from_inet():
    sort_test(odd_even_sort_from_inet)
