"""
Source: https://realpython.com/primer-on-python-decorators/#a-few-real-world-examples
"""

import functools


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            assert num_times > 0, 'num_times param must be positive value'
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=3)
def hello():
    print('Hello World')


hello()
# hello = repeat(3)(hello)