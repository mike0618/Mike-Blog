"""
Instructions
Create a logging_decorator() which is going to log the name of the function that was called,
the arguments it was given and finally the returned output.

Expected Output
https://cdn.fs.teachablecdn.com/jA2ypes2RfuB0cuC41yd
"""


# Create the logging_decorator() function
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}\nIt returned: {function(*args)}")

    return wrapper


# Use the decorator
@logging_decorator
def a_function1(a, b, c):
    return a + b + c


a_function1(1, 2, 3)


@logging_decorator
def a_function2(*args):
    return sum(args)


a_function2(1, 2, 3, 4)


@logging_decorator
def a_function3(*args):
    product = 1
    for n in args:
        product *= n
    return product


a_function3(1, 2, 3, 4)
