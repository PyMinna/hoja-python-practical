def greet_decorator(func):
    def wrapper():
        print("Befor greeting..")
        func()
        print("After greeting")

    return wrapper

@greet_decorator
def say_hello():
    print("hello...")

say_hello()