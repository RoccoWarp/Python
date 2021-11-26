def type_logger(func):
    def wrapper(*args):
        for arg in args:
            print(f'{func. __name__}({arg}:{type(arg)})')
        result = func(*args)
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
