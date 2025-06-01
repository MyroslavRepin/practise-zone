import time


def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        return end - start
    return wrapper


@timer
def set_timer():
    x = 0
    for i in range(10000):
        x += 1


print(set_timer())
