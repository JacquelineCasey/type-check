
import functools
from typing import Callable

# TODO:
# add real support for kwargs
# Should int and float get special cased?

def type_checked(func: Callable):
    
    @functools.wraps(func)
    def typed_wrapper(*args, **kwargs):
        for argument, parameter in zip(args, func.__code__.co_varnames):
            if not issubclass(type(argument), func.__annotations__[parameter]):
                raise TypeError(f"TypeError in function {func.__name__}().\n" + 
                    f"    Parameter {parameter} has type {func.__annotations__[parameter].__name__}, but was provided value {parameter} with type {type(parameter).__name__}") 

        return func(*args, **kwargs)

    return typed_wrapper

@type_checked
def square(a: int):
    return a * a

print(square(10))
print(square("Hello"))
