"""
    This famous sequence is recursive because each term after the second term is the sum of the previous two terms.
    Our first two terms are 1 and 1. The third term is the previous two terms added together, or 1+1=2.
    The next term is the addition of the two prior terms, or 1+2=3. And this pattern continues indefinitely.
"""

from typing import Tuple
from utils.profilers import Profiler


profiler_recursive = Profiler()
profiler_cycle = Profiler()


def fibonacci_recursive(n: int) -> Tuple[int, int]:
    profiler_recursive.amount += 1  # profiling

    if n in (0, 1):
        amount = profiler_recursive.amount  # profiling
        del profiler_recursive.amount  # profiling

        return 1, amount
    else:
        return tuple(x + y for x, y in zip(fibonacci_recursive(n - 2), fibonacci_recursive(n - 1)))


def fibonacci_cycle(n: int) -> Tuple[int, int]:
    previos_num = 0
    current_num = 1

    for i in range(n):
        previos_num, _ = current_num, previos_num
        current_num = _ + current_num

        profiler_cycle.amount += 1  # profiling

    amount = profiler_cycle.amount  # profiling
    del profiler_cycle.amount  # profiling

    return current_num, amount
