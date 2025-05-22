"""
Source: https://realpython.com/primer-on-python-decorators/#a-few-real-world-examples
"""

import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Function {func.__name__} finished in {run_time:.4f} sec!')
        return result
    return wrapper_timer


@timer
def delay_greeting(msg='Hello World!'):
    time.sleep(1)
    return msg


delay_greeting()
