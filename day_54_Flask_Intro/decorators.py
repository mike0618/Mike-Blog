from time import sleep


def delay_decorator(function):
    def wrapper():
        sleep(2)
        # Do something before
        function()
        function()
        # Do something after
        print("\n")

    return wrapper


@delay_decorator
def say_hello():
    print('hello')


@delay_decorator
def say_bye():
    print('bye')


def say_greeting():
    print('how are you?')


say_hello()

decorated_function = delay_decorator(say_greeting)
decorated_function()

say_bye()
