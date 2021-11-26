def value_checker(is_valid):
    def wrapper(func):
        def val_executor(*args):
            if is_valid(*args):
                result = func(*args)
                return result
            else:
                raise ValueError(f'Wrong value: {args}')

        return val_executor
    return wrapper


@value_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
