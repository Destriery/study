import cProfile
import pstats
from datetime import datetime
from typing import Callable
from functools import wraps


def profiler(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        result_time = datetime.now() - start_time

        print(result_time.total_seconds())

        return result

    return wrapper


class Profiler:
    _amount: int = 0
    result_time: float

    def __init__(self) -> None:
        self.cp = cProfile.Profile()

    def start(self):
        self.start_time = datetime.now()
        self.cp.enable()

    def stop(self):
        self.cp.disable()
        self.result_time = (datetime.now() - self.start_time).total_seconds()

    def print_stats(self):
        self.stats = pstats.Stats(self.cp).sort_stats('ncalls')
        self.stats.print_stats()

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, _amount):
        self._amount = _amount

    @amount.deleter
    def amount(self):
        self._amount = 0


def print_timit():
    # TODO сделать абстрактную функцию

    import timeit

    f = timeit.timeit(
        'odd_even(sorted([i for i in range(10)], key=lambda x: random.random()))',
        number=1000,
        globals=globals(),
        setup="import random"
    )
    s = timeit.timeit(
        'odd_even_sort_from_inet(sorted([i for i in range(10)], key=lambda x: random.random()))',
        number=1000,
        globals=globals(),
        setup="import random"
    )

    print(f)
    print(s)
