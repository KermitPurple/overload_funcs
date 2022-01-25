#!/usr/bin/env python3

from typing import Callable, ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')

def convert_annotations(dct: dict[str, type]) -> tuple[type, ...]:
    '''Convert an annotations dict into a tuple of argument types'''
    return tuple(val for key, val in dct.items() if key != 'return')

def get_type_tuple(*args) -> tuple[type, ...]:
    '''Convert all parameters into a tuple of types'''
    return tuple(map(type, args))

class OverloadFunction:
    '''A class that represents an overloaded function'''

    def __init__(self, name: str):
        self.__name__ = name
        self.overloaded: dict[tuple[type, ...], Callable[P, R]] = {}

    def load(self, func: Callable[P, R]):
        '''Add a function to the overloaded'''
        print(func.__annotations__)
        self.overloaded[convert_annotations(func.__annotations__)] = func
        return self

    def __call__(self, *args):
        '''Choose the correct version of the function to call'''
        types = get_type_tuple(*args)
        if types in self.overloaded:
            return self.overloaded[types](*args)
        else:
            raise ValueError(f'Function with signature {types} does not exist in overloaded')

    def __str__(self):
        return f'<OverloadFunction {self.__name__} at {hex(id(self))}>'

def overload(func: Callable[P, R]) -> OverloadFunction:
    '''A decorator that creates an OverloadFunction'''
    return OverloadFunction(func.__name__).load(func)
