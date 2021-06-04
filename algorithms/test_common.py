from utils.profilers import Profiler

from .fibonacci import fibonacci_recursive, fibonacci_cycle


FIBONACCI_MAPPING = {
        0: 1,
        1: 1,
        2: 2,
        3: 3,
        4: 5,
        5: 8,
        6: 13,
        7: 21,
        8: 34,
        9: 55,
        10: 89,
        12: 233,
        30: 1346269,
        # 35: 14930352
    }


profiler = Profiler()


def fibonacci(func):
    print('\n')

    for num, result in FIBONACCI_MAPPING.items():
        profiler.start()

        fibonacci_result = func(num)
        assert fibonacci_result[0] == result
        profiler.stop()

        print(num, ':', profiler.result_time, fibonacci_result[1])


def test__fibonacci_recursive():
    fibonacci(fibonacci_recursive)


def test__fibonacci_cycle():
    fibonacci(fibonacci_cycle)
