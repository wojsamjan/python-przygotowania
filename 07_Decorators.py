"""
Source: https://realpython.com/primer-on-python-decorators/#a-few-real-world-examples
"""
# Can you guess what happens when you call say_whee()? Try it in a REPL. 
# Instead of running the file with the -i flag, you can also import the function manually:

# So, @decorator is just a shorter way of saying say_hello = decorator(say_hello).

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def say_hello(name='Adam'):
    print(f'Running greating...')
    return f'Hello {name}'


print(say_hello('Wojtek'))
print(say_hello)
print(say_hello.__name__)
# print(help(say_hello))
