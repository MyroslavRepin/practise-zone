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
    for i in range(7000):
        x += 1


print(set_timer())


def logger(func):
    def wrapper():
        return f"Running function: {func.__name__}"
    return wrapper


@logger
def test_logger():
    """MY LOGGER"""
    print('Testing')


print(test_logger())


admin_rights = True


def check_admin(func):
    def wrapper():
        if admin_rights == False:
            return 'Acces denied'
        if admin_rights == True:
            return func()
    return wrapper


@check_admin
@timer
def delete_database():
    return 'Database deleted'


print(delete_database())
