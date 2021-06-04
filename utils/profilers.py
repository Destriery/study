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

    def start(self):
        self.start_time = datetime.now()

    def stop(self):
        self.result_time = (datetime.now() - self.start_time).total_seconds()

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, _amount):
        self._amount = _amount

    @amount.deleter
    def amount(self):
        self._amount = 0
